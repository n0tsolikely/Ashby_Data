# 03_VERIFY.md

## Raw Receipt Source
- See `06_TESTS.txt` for wrapper-captured raw command receipts.

## Verification Command
- CMD: `cd /home/notsolikely/Ashby_Engine && python3 tools/realtime_log_doctor.py --stuart-root "$HOME/ashby_runtime/stuart" --lines 400 && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_realtime_log_doctor.py`
- RESULT: `No alerts found in realtime logs` and `2 passed in 0.03s`
- RC: `0`

## Assertions Verified
- Doctor CLI reads local `events.jsonl` + `alerts.jsonl` without network access.
- Alerts are grouped by `correlation_id` with chain extraction from events.
- Likely-cause categorization is emitted from alert events.

OVERALL: PASS
