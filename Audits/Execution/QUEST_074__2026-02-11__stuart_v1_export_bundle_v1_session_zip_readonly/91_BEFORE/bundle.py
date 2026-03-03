from __future__ import annotations

import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from ashby.modules.meetings.init_root import init_stuart_root
from ashby.modules.meetings.manifests import load_manifest


_DETERMINISTIC_ZIP_DT = (2000, 1, 1, 0, 0, 0)


@dataclass(frozen=True)
class ExportBundleResult:
    session_id: str
    zip_path: str
    files_added: int

    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "zip_path": self.zip_path,
            "files_added": int(self.files_added),
        }


def _safe_rel(root: Path, p: Path) -> Optional[str]:
    """Return a normalized posix relative path inside the bundle.

    Rails:
    - bundle content MUST be under STUART_ROOT
    - we never include absolute paths
    """
    try:
        rel = p.resolve().relative_to(root.resolve())
    except Exception:
        return None
    return rel.as_posix()


def _iter_files_recursive(dir_path: Path) -> Iterable[Path]:
    for p in sorted(dir_path.rglob("*")):
        if p.is_file():
            yield p


def _collect_session_files(session_id: str) -> List[Path]:
    lay = init_stuart_root()
    root = lay.root

    out: List[Path] = []

    # Session manifests
    sess_dir = lay.sessions / session_id
    out.append(sess_dir / "session.json")
    st = sess_dir / "session_state.json"
    if st.exists():
        out.append(st)

    # Overlays (speaker_map only for now)
    ovr_dir = lay.overlays / session_id
    if ovr_dir.exists():
        out.extend([p for p in _iter_files_recursive(ovr_dir)])

    # Contributions: scan and match session_id
    if lay.contributions.exists():
        for con_dir in sorted(lay.contributions.iterdir()):
            if not con_dir.is_dir():
                continue
            man = con_dir / "contribution.json"
            if not man.exists():
                continue
            try:
                c = load_manifest(man)
            except Exception:
                continue
            if c.get("session_id") != session_id:
                continue
            out.append(man)
            # Include all other files in the contribution dir (source, derived_audio, etc.)
            for p in sorted(con_dir.iterdir()):
                if p.is_file() and p.name != "contribution.json":
                    out.append(p)

    # Runs: scan and match session_id
    if lay.runs.exists():
        for run_dir in sorted(lay.runs.iterdir()):
            if not run_dir.is_dir():
                continue
            run_json = run_dir / "run.json"
            if not run_json.exists():
                continue
            try:
                r = load_manifest(run_json)
            except Exception:
                continue
            if r.get("session_id") != session_id:
                continue

            out.append(run_json)
            ev = run_dir / "events.jsonl"
            if ev.exists():
                out.append(ev)

            art_dir = run_dir / "artifacts"
            if art_dir.exists():
                out.extend(list(_iter_files_recursive(art_dir)))

    # Filter to files that exist (some optional paths above)
    return [p for p in out if p.exists() and p.is_file()]


def export_session_bundle(
    session_id: str,
    *,
    out_dir: Optional[Path] = None,
    out_path: Optional[Path] = None,
) -> ExportBundleResult:
    """Create a read-only zip bundle of a session's manifests + artifacts.

    Contract (D5 / QUEST_067):
    - returns a zip path
    - no mutation of canonical store

    Notes:
    - This is a minimal v1 export to unblock CLI usage.
    - A fuller spec lives in QUEST_074.

    Determinism rails:
    - files are written in sorted order
    - zip timestamps and perms are normalized
    - output path uses session created date (UTC) when not specified
    """
    lay = init_stuart_root()
    root = lay.root

    sess_json = lay.sessions / session_id / "session.json"
    if not sess_json.exists():
        raise FileNotFoundError(f"Unknown session_id (missing manifest): {sess_json}")

    sess = load_manifest(sess_json)
    created_ts = sess.get("created_ts")
    if not isinstance(created_ts, (int, float)):
        created_ts = None

    if out_path is None:
        if out_dir is None:
            out_dir = lay.exports
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        if created_ts is None:
            # deterministic fallback: literal string (no current-time dependence)
            date_str = "unknown_date"
        else:
            dt = datetime.fromtimestamp(float(created_ts), tz=timezone.utc)
            date_str = dt.strftime("%Y%m%d")

        out_path = out_dir / f"{session_id}__export_bundle__{date_str}.zip"

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files = _collect_session_files(session_id)

    items: List[Tuple[Path, str]] = []
    for p in files:
        rel = _safe_rel(root, p)
        if not rel:
            continue
        # Guard: never include exports/ (avoid recursive bundle of prior bundles)
        if rel.startswith("exports/"):
            continue
        items.append((p, rel))

    # Deterministic ordering
    items.sort(key=lambda t: t[1])

    # Create zip without overwrite
    with zipfile.ZipFile(out_path, mode="x", compression=zipfile.ZIP_DEFLATED) as z:
        for src, arc in items:
            data = src.read_bytes()
            zi = zipfile.ZipInfo(filename=arc, date_time=_DETERMINISTIC_ZIP_DT)
            # Normalize perms (rw-r--r--)
            zi.external_attr = (0o644 & 0xFFFF) << 16
            z.writestr(zi, data)

    return ExportBundleResult(session_id=session_id, zip_path=str(out_path), files_added=len(items))
