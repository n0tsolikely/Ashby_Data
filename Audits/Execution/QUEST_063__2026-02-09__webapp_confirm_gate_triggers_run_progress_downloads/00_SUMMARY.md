# QUEST_063 — webapp_confirm_gate_triggers_run_progress_downloads

Date: 2026-02-09

## What changed
We tightened the Web Door “confirm → run → progress → download” loop so it is **codex-true and deterministic**:

- `/api/runs/{run_id}` now returns:
  - `progress`: a small polling payload (`status`, `stage`, `progress`, timestamps)
  - `downloads`: deterministic links for primary outputs derived from `run.json["primary_outputs"]`
  - `artifacts`: full listing (debug / secondary)

- Web Door UI now:
  - Shows a live **Run Status** card (status/stage/progress)
  - Shows **Primary Outputs** (PDF/MD/JSON/evidence) using `primary_outputs` pointers (no guessed filenames)
  - Uses a clearer confirm label: **“Confirm & Run”**

## Why
Dungeon 5 requires explicit execution gating and deterministic output surfacing:
- Upload ≠ process (already done in QUEST_062)
- Confirm triggers the run
- Progress is visible
- Download links must be derived from run manifests (no filename heuristics)

## Files changed
- `Ashby_Engine/ashby/interfaces/web/app.py`
- `Ashby_Engine/ashby/interfaces/web/runs.py`
- `Ashby_Engine/ashby/interfaces/web/static/app.js`
- `Ashby_Engine/tests/test_meetings_web_upload_run.py`

## Tests
- `python3 -m pytest -q` (PASS)

Artifacts:
- `05_DIFF.patch`
- `06_PYTEST_-q.txt`
