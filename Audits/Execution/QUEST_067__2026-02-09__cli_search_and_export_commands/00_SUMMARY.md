# QUEST_067 — CLI search + export commands

Date: 2026-02-09
Status: COMPLETE

## What changed
- Added **CLI library search**: `stuart search <query>` with optional `--session` and `--mode` filters.
  - Output is **sessions-first** (ranked sessions, with per-session hits).
  - Each hit includes a **snippet** and a **citation anchor** (session_id/run_id/segment_id + optional timestamps).
  - CLI search does **not** create runs and does **not** auto-open artifacts.

- Added **CLI export**: `stuart export --session <id>`.
  - Creates a **read-only zip bundle** under `STUART_ROOT/exports/` (or `--out <path>`).

## Files changed / added
Engine:
- `ashby/modules/meetings/cli_stuart.py` (updated search UX + added export command)
- `ashby/modules/meetings/export/__init__.py` (new)
- `ashby/modules/meetings/export/bundle.py` (new export bundler)

Tests:
- `tests/test_meetings_cli_search_export.py` (new)

Data:
- Quest moved: `Quest Board/Accepted/...QUEST_067...` → `Quest Board/Completed/...QUEST_067...`

## Verification
Smoke gate (captured):
- `06_PYTEST_smoke_gate_-q.txt` (exit code in `06_PYTEST_smoke_gate_-q.exitcode`)

Diffs:
- `05_DIFF_Ashby_Engine.patch`
- `05_DIFF_Ashby_Data.patch`
