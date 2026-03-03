# SIDE-QUEST_030 — Stuart Runner Subprocess PYTHONPATH Import Fix

Date (local): 2026-02-02
Status: COMPLETED (PASS)

What this quest is
- Fix Stuart runner subprocess import reliability by ensuring repo root is injected into subprocess PYTHONPATH.

Why this exists
- Stuart doors (web/telegram) shell out to `python -m ashby.modules.meetings.cli_stuart ...` via `ashby/interfaces/telegram/stuart_runner.py`.
- If the parent process is launched outside the repo root and without PYTHONPATH set, the subprocess can fail:
  `ModuleNotFoundError: No module named 'ashby'`

Planned change (smallest correct)
- Fix `ashby/interfaces/telegram/stuart_runner.py` so `_env()`:
  - does not throw NameError
  - prepends repo root to env["PYTHONPATH"] deterministically

Verification bar (PASS required)
- `_env()` returns env with PYTHONPATH containing repo root.
- `run_default_pipeline()` succeeds when parent clears PYTHONPATH env (no external hacks).
- `python3 -m pytest -q` passes.
