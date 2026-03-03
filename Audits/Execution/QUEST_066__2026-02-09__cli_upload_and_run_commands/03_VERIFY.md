# QUEST_066 — Verification

Date: 2026-02-09

## Smoke gate executed (real)
Command executed from `/mnt/data/Ashby_Engine`:

```bash
PYTHONPATH=/mnt/data/Ashby_Engine python -m pytest -q \
  tests/test_meetings_cli_stuart.py \
  tests/test_meetings_web_door_scaffold.py \
  tests/test_meetings_web_upload_run.py \
  tests/test_telegram_stuart_door_core.py \
  tests/test_telegram_stuart_runner_smoke.py
```

Result:
- Exit code: `0`
- `10 passed`

Artifacts:
- Full output: `06_PYTEST_smoke_-q.txt`
- Exit code: `06_PYTEST_smoke_-q.exitcode`
