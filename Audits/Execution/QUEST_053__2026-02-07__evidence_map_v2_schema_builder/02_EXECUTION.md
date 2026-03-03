# QUEST_053 — Execution

Date: 2026-02-07

## Step 1 — Added v2 schema + validator
- Added: `ashby/modules/meetings/schemas/evidence_map_v2.py`

## Step 2 — Upgraded evidence builder to v2
- Updated: `ashby/modules/meetings/render/evidence_map.py`
- Behavior changes:
  - `version: 2`
  - Claims derive from minutes/journal items (topic/decision/action/etc)
  - Anchors resolve from cited `segment_id` → transcript segment (`t_start`, `t_end`, `speaker_label`)
  - Still write-once (refuses overwrite)

## Step 3 — Updated tests
- Updated evidence_map version assertions to expect v2.

## Diffs

### NEW — evidence_map_v2 schema
```diff
--- /dev/null	2026-02-07 11:37:30.186254277 +0000
+++ /mnt/data/Ashby_Engine/ashby/modules/meetings/schemas/evidence_map_v2.py	2026-02-07 11:59:46.227904914 +0000
@@ -0,0 +1,133 @@
+from __future__ import annotations
+
+from typing import Any, Dict, List, TypedDict
+
+from ashby.modules.meetings.schemas.artifacts_v1 import require_keys
+
+
+# ----------------------------
+# evidence_map.json — v2 machine contract
+# ----------------------------
+# Purpose:
+# - Provide claim-level anchors tying minutes/journal claims to transcript segments.
+# - This is NOT external fact checking. It is traceability.
+
+
+class EvidenceAnchorV2(TypedDict, total=False):
+    # Required
+    segment_id: int
+    t_start: float
+    t_end: float
+    speaker_label: str
+
+
+class EvidenceSourceV2(TypedDict, total=False):
+    # Where the claim came from (minutes.json / journal.json)
+    artifact: str  # "minutes.json" | "journal.json"
+    item_type: str  # e.g. topic|decision|action_item|note|open_question|narrative|key_point|feeling
+    item_id: str
+
+
+class EvidenceClaimV2(TypedDict, total=False):
+    # Required
+    claim_id: str
+    claim_type: str  # e.g. minutes.topic, minutes.decision, journal.narrative
+    claim_text: str
+    anchors: List[EvidenceAnchorV2]
+
+    # Optional helpers
+    title: str
+    source: EvidenceSourceV2
+
+
+class EvidenceMapV2(TypedDict):
+    version: int
+    session_id: str
+    run_id: str
+    mode: str  # meeting|journal
+    claims: List[EvidenceClaimV2]
+
+
+def _validate_anchor(a: Any) -> None:
+    if not isinstance(a, dict):
+        raise ValueError("evidence anchor must be an object")
+
+    for k in ("segment_id", "t_start", "t_end", "speaker_label"):
+        if k not in a:
+            raise ValueError(f"evidence anchor missing required key: {k}")
+
+    try:
+        sid = int(a["segment_id"])
+    except Exception:
+        raise ValueError("evidence anchor segment_id must be int")
+    if sid < 0:
+        raise ValueError("evidence anchor segment_id must be >= 0")
+
+    try:
+        float(a["t_start"])
+        float(a["t_end"])
+    except Exception:
+        raise ValueError("evidence anchor t_start/t_end must be float")
+
+    if not isinstance(a.get("speaker_label"), str) or not a.get("speaker_label"):
+        raise ValueError("evidence anchor speaker_label must be a non-empty string")
+
+
+def _validate_claim(c: Any) -> None:
+    if not isinstance(c, dict):
+        raise ValueError("evidence claim must be an object")
+
+    for k in ("claim_id", "claim_type", "claim_text", "anchors"):
+        if k not in c:
+            raise ValueError(f"evidence claim missing required key: {k}")
+
+    if not isinstance(c.get("claim_id"), str) or not c.get("claim_id"):
+        raise ValueError("evidence claim_id must be a non-empty string")
+
+    if not isinstance(c.get("claim_type"), str) or not c.get("claim_type"):
+        raise ValueError("evidence claim_type must be a non-empty string")
+
+    if not isinstance(c.get("claim_text"), str):
+        raise ValueError("evidence claim_text must be a string")
+
+    anchors = c.get("anchors")
+    if not isinstance(anchors, list):
+        raise ValueError("evidence claim anchors must be a list")
+
+    # anchors MAY be empty (e.g., optional-citation narrative sections), but if present must be valid.
+    for a in anchors:
+        _validate_anchor(a)
+
+
+def validate_evidence_map_v2(payload: Dict[str, Any]) -> None:
+    """Validate evidence_map.json v2.
+
+    Requirements:
+    - version == 2
+    - required top-level keys exist
+    - claims are claim-level objects with transcript anchors
+
+    Note:
+    - This validates traceability structure, not external truth.
+    """
+
+    require_keys(payload, ["version", "session_id", "run_id", "mode", "claims"])
+
+    if int(payload["version"]) != 2:
+        raise ValueError("EvidenceMapV2 version must be 2")
+
+    if not isinstance(payload.get("session_id"), str):
+        raise ValueError("EvidenceMapV2 session_id must be a string")
+
+    if not isinstance(payload.get("run_id"), str):
+        raise ValueError("EvidenceMapV2 run_id must be a string")
+
+    if not isinstance(payload.get("mode"), str) or not payload.get("mode"):
+        raise ValueError("EvidenceMapV2 mode must be a non-empty string")
+
+    claims = payload.get("claims")
+    if not isinstance(claims, list):
+        raise ValueError("EvidenceMapV2 claims must be a list")
+
+    for c in claims:
+        _validate_claim(c)
```

### UPDATED — evidence_map builder (v1 → v2)
```diff
--- /dev/fd/63	2026-02-07 12:18:27.234840851 +0000
+++ /mnt/data/Ashby_Engine/ashby/modules/meetings/render/evidence_map.py	2026-02-07 12:03:38.620455527 +0000
@@ -3,19 +3,22 @@
 import json
 import time
 from pathlib import Path
-from typing import Any, Dict, List
+from typing import Any, Dict, List, Optional, Tuple
 
 from ashby.modules.meetings.schemas.artifacts_v1 import dump_json
+from ashby.modules.meetings.schemas.evidence_map_v2 import validate_evidence_map_v2
 from ashby.modules.meetings.store import sha256_file
 
 
-def _load_segments(run_dir: Path, *, mode: str) -> List[Dict[str, Any]]:
+def _load_transcript_payload(run_dir: Path, *, mode: str) -> Tuple[str, str, List[Dict[str, Any]]]:
     """Load transcript segments for evidence anchoring.
 
     Preference:
     - meeting: aligned_transcript.json if present
     - else: transcript.json if present
     - else: transcript.txt lines as SPEAKER_00 (no timestamps)
+
+    Returns (session_id, run_id, segments).
     """
     artifacts = run_dir / "artifacts"
     ajson = artifacts / "aligned_transcript.json"
@@ -24,57 +27,277 @@
 
     if mode == "meeting" and ajson.exists():
         payload = json.loads(ajson.read_text(encoding="utf-8"))
-        return list(payload.get("segments") or [])
+        return (
+            str(payload.get("session_id") or ""),
+            str(payload.get("run_id") or run_dir.name),
+            list(payload.get("segments") or []),
+        )
 
     if tjson.exists():
         payload = json.loads(tjson.read_text(encoding="utf-8"))
-        return list(payload.get("segments") or [])
+        return (
+            str(payload.get("session_id") or ""),
+            str(payload.get("run_id") or run_dir.name),
+            list(payload.get("segments") or []),
+        )
 
+    # Fallback to transcript.txt (no timestamps) — still truthfully anchored by line order.
     segs: List[Dict[str, Any]] = []
     if ttxt.exists():
         for i, line in enumerate(ttxt.read_text(encoding="utf-8", errors="replace").splitlines()):
             s = line.strip()
             if not s:
                 continue
-            segs.append({"segment_id": i, "start_ms": 0, "end_ms": 0, "speaker": "SPEAKER_00", "text": s})
-    return segs
+            segs.append(
+                {
+                    "segment_id": int(i),
+                    "start_ms": 0,
+                    "end_ms": 0,
+                    "speaker": "SPEAKER_00",
+                    "text": s,
+                }
+            )
+    return ("", run_dir.name, segs)
 
 
-def _anchors_from_segments(segs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
-    """Minimal v1 anchors: first and last segment (or just first)."""
-    if not segs:
-        return []
-    first = segs[0]
-    last = segs[-1]
-    chosen = (first, last) if last is not first else (first,)
+def _segment_index(segs: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
+    out: Dict[int, Dict[str, Any]] = {}
+    for i, s in enumerate(segs):
+        try:
+            sid = int(s.get("segment_id", i))
+        except Exception:
+            sid = int(i)
+        out[sid] = s
+    return out
+
+
+def _anchor_from_segment(seg: Optional[Dict[str, Any]], *, segment_id: int) -> Dict[str, Any]:
+    if not isinstance(seg, dict):
+        # Unknown segment => truthful minimal anchor
+        return {
+            "segment_id": int(segment_id),
+            "t_start": 0.0,
+            "t_end": 0.0,
+            "speaker_label": "SPEAKER_00",
+        }
+
+    try:
+        t0 = float(seg.get("start_ms", 0)) / 1000.0
+    except Exception:
+        t0 = 0.0
+    try:
+        t1 = float(seg.get("end_ms", 0)) / 1000.0
+    except Exception:
+        t1 = 0.0
+
+    spk = seg.get("speaker")
+    speaker_label = str(spk or "SPEAKER_00")
+
+    return {
+        "segment_id": int(segment_id),
+        "t_start": float(t0),
+        "t_end": float(t1),
+        "speaker_label": speaker_label,
+    }
+
+
+def _anchors_from_citations(citations: Any, segs_by_id: Dict[int, Dict[str, Any]]) -> List[Dict[str, Any]]:
     anchors: List[Dict[str, Any]] = []
-    for s in chosen:
-        anchors.append(
+    if not isinstance(citations, list):
+        return anchors
+
+    for c in citations:
+        if not isinstance(c, dict) or "segment_id" not in c:
+            continue
+        try:
+            sid = int(c["segment_id"])
+        except Exception:
+            continue
+        anchors.append(_anchor_from_segment(segs_by_id.get(sid), segment_id=sid))
+    return anchors
+
+
+def _claims_from_minutes(minutes_payload: Dict[str, Any], segs_by_id: Dict[int, Dict[str, Any]]) -> List[Dict[str, Any]]:
+    claims: List[Dict[str, Any]] = []
+
+    for t in minutes_payload.get("topics") or []:
+        if not isinstance(t, dict):
+            continue
+        tid = str(t.get("topic_id") or "")
+        claims.append(
             {
-                "segment_id": int(s.get("segment_id", 0)),
-                "t_start": float(s.get("start_ms", 0)) / 1000.0,
-                "t_end": float(s.get("end_ms", 0)) / 1000.0,
-                "speaker_label": str(s.get("speaker") or "SPEAKER_00"),
+                "claim_id": f"minutes.topic.{tid}" if tid else "minutes.topic",
+                "claim_type": "minutes.topic",
+                "claim_text": str(t.get("summary") or ""),
+                "title": str(t.get("title") or ""),
+                "source": {"artifact": "minutes.json", "item_type": "topic", "item_id": tid},
+                "anchors": _anchors_from_citations(t.get("citations"), segs_by_id),
+            }
+        )
+
+    for d in minutes_payload.get("decisions") or []:
+        if not isinstance(d, dict):
+            continue
+        did = str(d.get("decision_id") or "")
+        claims.append(
+            {
+                "claim_id": f"minutes.decision.{did}" if did else "minutes.decision",
+                "claim_type": "minutes.decision",
+                "claim_text": str(d.get("text") or ""),
+                "source": {"artifact": "minutes.json", "item_type": "decision", "item_id": did},
+                "anchors": _anchors_from_citations(d.get("citations"), segs_by_id),
+            }
+        )
+
+    for a in minutes_payload.get("action_items") or []:
+        if not isinstance(a, dict):
+            continue
+        aid = str(a.get("action_id") or "")
+        claims.append(
+            {
+                "claim_id": f"minutes.action_item.{aid}" if aid else "minutes.action_item",
+                "claim_type": "minutes.action_item",
+                "claim_text": str(a.get("text") or ""),
+                "source": {"artifact": "minutes.json", "item_type": "action_item", "item_id": aid},
+                "anchors": _anchors_from_citations(a.get("citations"), segs_by_id),
+            }
+        )
+
+    for n in minutes_payload.get("notes") or []:
+        if not isinstance(n, dict):
+            continue
+        nid = str(n.get("note_id") or "")
+        claims.append(
+            {
+                "claim_id": f"minutes.note.{nid}" if nid else "minutes.note",
+                "claim_type": "minutes.note",
+                "claim_text": str(n.get("text") or ""),
+                "source": {"artifact": "minutes.json", "item_type": "note", "item_id": nid},
+                "anchors": _anchors_from_citations(n.get("citations"), segs_by_id),
+            }
+        )
+
+    for q in minutes_payload.get("open_questions") or []:
+        if not isinstance(q, dict):
+            continue
+        qid = str(q.get("question_id") or "")
+        claims.append(
+            {
+                "claim_id": f"minutes.open_question.{qid}" if qid else "minutes.open_question",
+                "claim_type": "minutes.open_question",
+                "claim_text": str(q.get("text") or ""),
+                "source": {"artifact": "minutes.json", "item_type": "open_question", "item_id": qid},
+                "anchors": _anchors_from_citations(q.get("citations"), segs_by_id),
             }
         )
-    return anchors
+
+    return claims
+
+
+def _claims_from_journal(journal_payload: Dict[str, Any], segs_by_id: Dict[int, Dict[str, Any]]) -> List[Dict[str, Any]]:
+    claims: List[Dict[str, Any]] = []
+
+    for s in journal_payload.get("narrative_sections") or []:
+        if not isinstance(s, dict):
+            continue
+        sid = str(s.get("section_id") or "")
+        claims.append(
+            {
+                "claim_id": f"journal.narrative.{sid}" if sid else "journal.narrative",
+                "claim_type": "journal.narrative",
+                "claim_text": str(s.get("text") or ""),
+                "title": str(s.get("title") or ""),
+                "source": {"artifact": "journal.json", "item_type": "narrative", "item_id": sid},
+                "anchors": _anchors_from_citations(s.get("citations"), segs_by_id),
+            }
+        )
+
+    for kp in journal_payload.get("key_points") or []:
+        if not isinstance(kp, dict):
+            continue
+        pid = str(kp.get("point_id") or "")
+        claims.append(
+            {
+                "claim_id": f"journal.key_point.{pid}" if pid else "journal.key_point",
+                "claim_type": "journal.key_point",
+                "claim_text": str(kp.get("text") or ""),
+                "source": {"artifact": "journal.json", "item_type": "key_point", "item_id": pid},
+                "anchors": _anchors_from_citations(kp.get("citations"), segs_by_id),
+            }
+        )
+
+    for a in journal_payload.get("action_items") or []:
+        if not isinstance(a, dict):
+            continue
+        aid = str(a.get("action_id") or "")
+        claims.append(
+            {
+                "claim_id": f"journal.action_item.{aid}" if aid else "journal.action_item",
+                "claim_type": "journal.action_item",
+                "claim_text": str(a.get("text") or ""),
+                "source": {"artifact": "journal.json", "item_type": "action_item", "item_id": aid},
+                "anchors": _anchors_from_citations(a.get("citations"), segs_by_id),
+            }
+        )
+
+    for f in journal_payload.get("feelings") or []:
+        if not isinstance(f, dict):
+            continue
+        txt = str(f.get("text") or "")
+        # Feelings may omit citations; still represented (anchors may be empty)
+        claims.append(
+            {
+                "claim_id": "journal.feeling",
+                "claim_type": "journal.feeling",
+                "claim_text": txt,
+                "source": {"artifact": "journal.json", "item_type": "feeling", "item_id": ""},
+                "anchors": _anchors_from_citations(f.get("citations"), segs_by_id),
+            }
+        )
+
+    return claims
+
+
+def _fallback_transcript_claim(segs: List[Dict[str, Any]], segs_by_id: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
+    # Minimal truthful claim when no minutes/journal artifacts exist.
+    if not segs:
+        anchors: List[Dict[str, Any]] = []
+    else:
+        first = segs[0]
+        last = segs[-1]
+        anchors = []
+        for s in (first, last) if last is not first else (first,):
+            try:
+                sid = int(s.get("segment_id", 0))
+            except Exception:
+                sid = 0
+            anchors.append(_anchor_from_segment(segs_by_id.get(sid), segment_id=sid))
+
+    return {
+        "claim_id": "transcript",
+        "claim_type": "transcript.section",
+        "claim_text": "Transcript section",
+        "anchors": anchors,
+    }
 
 
 def build_evidence_map(run_dir: Path) -> Dict[str, Any]:
-    """Build and write evidence_map.json deterministically (v1).
+    """Build and write evidence_map.json deterministically (v2).
 
-    V1 minimal:
-    - one claim for Transcript section
-    - anchors to real transcript segments/timestamps
+    V2:
+    - claim-level anchors
+    - claims derived from minutes.json or journal.json
+    - anchors resolve to transcript segments (segment_id + time range + speaker label)
+
+    Naming:
+    - Keep artifact name stable: artifacts/evidence_map.json
+    - Version is inside file.
     """
+
     out_path = run_dir / "artifacts" / "evidence_map.json"
     if out_path.exists():
         raise FileExistsError(f"Refusing to overwrite evidence_map: {out_path}")
 
-    # Derive session_id/run_id from paths (consistent with other artifacts)
-    session_id = run_dir.parent.parent.name if run_dir.parent.name == "runs" else ""
-    run_id = run_dir.name
-
     # Attempt to infer mode from run manifest if available; fallback meeting
     mode = "meeting"
     run_json = run_dir / "run.json"
@@ -85,28 +308,49 @@
         except Exception:
             pass
 
-    segs = _load_segments(run_dir, mode=mode)
-    anchors = _anchors_from_segments(segs)
+    session_id_t, run_id_t, segs = _load_transcript_payload(run_dir, mode=mode)
+    segs_by_id = _segment_index(segs)
+
+    artifacts = run_dir / "artifacts"
+
+    claims: List[Dict[str, Any]] = []
+    session_id = session_id_t
+    run_id = run_id_t
+
+    if mode == "meeting":
+        minutes_path = artifacts / "minutes.json"
+        if minutes_path.exists():
+            minutes_payload = json.loads(minutes_path.read_text(encoding="utf-8"))
+            session_id = str(minutes_payload.get("session_id") or session_id)
+            run_id = str(minutes_payload.get("run_id") or run_id)
+            claims = _claims_from_minutes(minutes_payload, segs_by_id)
+
+    elif mode == "journal":
+        journal_path = artifacts / "journal.json"
+        if journal_path.exists():
+            journal_payload = json.loads(journal_path.read_text(encoding="utf-8"))
+            session_id = str(journal_payload.get("session_id") or session_id)
+            run_id = str(journal_payload.get("run_id") or run_id)
+            claims = _claims_from_journal(journal_payload, segs_by_id)
+
+    if not claims:
+        claims = [_fallback_transcript_claim(segs, segs_by_id)]
 
-    # Must be non-empty anchors when segments exist; if segments empty, anchors empty (truthful).
     payload: Dict[str, Any] = {
-        "version": 1,
+        "version": 2,
         "session_id": session_id,
         "run_id": run_id,
-        "claims": [
-            {
-                "claim_id": "transcript",
-                "claim_text": "Transcript section",
-                "anchors": anchors,
-            }
-        ],
+        "mode": mode,
+        "claims": claims,
     }
 
+    validate_evidence_map_v2(payload)
     dump_json(out_path, payload, write_once=True)
+
     return {
         "kind": "evidence_map",
         "path": str(out_path),
         "sha256": sha256_file(out_path),
         "created_ts": time.time(),
-        "version": 1,
+        "version": 2,
     }
```

### UPDATED — tests/test_meetings_evidence_map_anchors.py
```diff
--- /dev/fd/63	2026-02-07 12:18:27.301074731 +0000
+++ /mnt/data/Ashby_Engine/tests/test_meetings_evidence_map_anchors.py	2026-02-07 12:04:27.546015185 +0000
@@ -34,12 +34,18 @@
     assert ev is not None
 
     payload = json.loads(Path(ev["path"]).read_text(encoding="utf-8"))
-    assert payload["version"] == 1
+    assert payload["version"] == 2
     claims = payload.get("claims") or []
     assert len(claims) >= 1
-    anchors = claims[0].get("anchors") or []
-    # must be non-empty and contain required fields
-    assert len(anchors) >= 1
+
+    # Find at least one claim with anchors (journal narrative sections can be uncited).
+    anchors = None
+    for c in claims:
+        a = c.get("anchors") if isinstance(c, dict) else None
+        if isinstance(a, list) and len(a) > 0:
+            anchors = a
+            break
+    assert anchors is not None
     a0 = anchors[0]
     assert "segment_id" in a0
     assert "t_start" in a0
```

### UPDATED — tests/test_meetings_render_md_pdf_evidence.py
```diff
--- /dev/fd/63	2026-02-07 12:18:27.321441831 +0000
+++ /mnt/data/Ashby_Engine/tests/test_meetings_render_md_pdf_evidence.py	2026-02-07 12:04:50.090362220 +0000
@@ -85,5 +85,5 @@
     assert not (run_dir / "exports" / "formalized.pdf").exists()
 
     payload = json.loads(ev_path.read_text(encoding="utf-8"))
-    assert payload["version"] == 1
+    assert payload["version"] == 2
     assert "claims" in payload
```

### UPDATED — tests/test_meetings_render_journal_md_pdf_evidence.py
```diff
--- /dev/fd/63	2026-02-07 12:18:27.400474687 +0000
+++ /mnt/data/Ashby_Engine/tests/test_meetings_render_journal_md_pdf_evidence.py	2026-02-07 12:05:00.419746966 +0000
@@ -83,5 +83,5 @@
     assert "## Narrative" in md_txt
 
     payload = json.loads(ev_path.read_text(encoding="utf-8"))
-    assert payload["version"] == 1
+    assert payload["version"] == 2
     assert "claims" in payload
```
