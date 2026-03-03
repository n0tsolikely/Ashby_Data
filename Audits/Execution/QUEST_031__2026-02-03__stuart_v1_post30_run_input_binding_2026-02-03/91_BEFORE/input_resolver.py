from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

from ashby.modules.meetings.store import Layout

@dataclass(frozen=True)
class ResolvedInput:
    contribution_id: str
    source_path: Path
    source_kind: str  # "audio" | "video" | etc.

def _load_contribution_json(contrib_dir: Path) -> dict:
    p = contrib_dir / "contribution.json"
    return json.loads(p.read_text(encoding="utf-8"))

def resolve_input_contribution(
    *,
    session_id: str,
    layout: Layout,
    contribution_id: Optional[str] = None,
) -> ResolvedInput:
    """Resolve which contribution should be processed for a run.

    Rule:
    - If contribution_id is provided -> validate and return it.
    - Else -> pick the latest contribution for session by created_ts in contribution.json.
    """
    # Validate explicit
    if contribution_id:
        con_dir = layout.contributions / contribution_id
        if not con_dir.exists():
            raise FileNotFoundError(f"contribution_id not found: {contribution_id}")
        meta = _load_contribution_json(con_dir)
        src = con_dir / meta.get("source_name", "source.bin")
        if not src.exists():
            # fallback: first source.* file
            cand = next(iter(con_dir.glob("source.*")), None)
            if not cand:
                raise FileNotFoundError(f"source file missing for contribution_id: {contribution_id}")
            src = cand
        return ResolvedInput(contribution_id=contribution_id, source_path=src, source_kind=str(meta.get("source_kind", "")))

    # Pick latest by created_ts
    latest: Tuple[float, str, Path, str] | None = None
    for con_dir in layout.contributions.iterdir():
        if not con_dir.is_dir():
            continue
        try:
            meta = _load_contribution_json(con_dir)
            if meta.get("session_id") != session_id:
                continue
            created = float(meta.get("created_ts", 0.0))
            src = con_dir / meta.get("source_name", "source.bin")
            if not src.exists():
                cand = next(iter(con_dir.glob("source.*")), None)
                if cand:
                    src = cand
            kind = str(meta.get("source_kind", ""))
            if latest is None or created > latest[0]:
                latest = (created, con_dir.name, src, kind)
        except Exception:
            continue

    if latest is None:
        raise FileNotFoundError(f"no contributions found for session_id: {session_id}")

    _, cid, src, kind = latest
    return ResolvedInput(contribution_id=cid, source_path=src, source_kind=kind)
