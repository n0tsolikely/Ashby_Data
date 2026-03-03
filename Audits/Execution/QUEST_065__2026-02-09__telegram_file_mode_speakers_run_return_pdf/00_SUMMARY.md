# QUEST_065 — SUMMARY

Date: 2026-02-09

## What shipped
- **Telegram door now requires an explicit confirm** after mode + speakers selection (no auto-run).
- **Door selections normalize through the unified `RunRequest` contract** (e.g. "2" -> 2, "3+" -> 3), so speakers hints are valid for downstream validation and diarization policy.
- **Telegram runner now returns the canonical mode-specific PDF** via `run.primary_outputs.pdf.path`:
  - meeting -> `minutes.pdf`
  - journal -> `journal.pdf`
- Added a minimal **subprocess runner smoke test** to guard the Telegram upload/plan/go wiring.

## Key behavior changes
- Uploading a file in Telegram:
  1) prompts **mode**
  2) prompts **speakers**
  3) prompts **confirm** (Confirm & Run / Cancel)
  4) only then runs the pipeline and returns the correct primary PDF

## Files changed
- `Ashby_Engine/ashby/interfaces/telegram/stuart_door_core.py`
- `Ashby_Engine/io/telegram/ashby_telegram_control.py`
- `Ashby_Engine/ashby/interfaces/telegram/stuart_runner.py`
- `Ashby_Engine/tests/test_telegram_stuart_door_core.py`
- `Ashby_Engine/tests/test_telegram_stuart_runner_smoke.py` (new)

## Tests
Smoke gate executed (see `06_PYTEST_smoke_-q.txt`):
- `tests/test_meetings_cli_stuart.py`
- `tests/test_meetings_web_door_scaffold.py`
- `tests/test_meetings_web_upload_run.py`
- `tests/test_telegram_stuart_door_core.py`
- `tests/test_telegram_stuart_runner_smoke.py`
