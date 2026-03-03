# Verify

## Smoke gate executed
```bash
cd /mnt/data/Ashby_Engine
PYTHONPATH=/mnt/data/Ashby_Engine python -m pytest -q \
  tests/test_meetings_cli_stuart.py \
  tests/test_meetings_web_door_scaffold.py \
  tests/test_meetings_web_upload_run.py \
  tests/test_telegram_stuart_door_core.py \
  tests/test_meetings_cli_search_export.py
```

Results:
- Output: `06_PYTEST_smoke_gate_-q.txt`
- Exit code: `06_PYTEST_smoke_gate_-q.exitcode` (expected `0`)

## Local CLI behavior validated by tests
- Search:
  - builds an index-backed session list + snippets + citations
  - does **not** create a run
- Export:
  - emits a zip bundle with expected paths
