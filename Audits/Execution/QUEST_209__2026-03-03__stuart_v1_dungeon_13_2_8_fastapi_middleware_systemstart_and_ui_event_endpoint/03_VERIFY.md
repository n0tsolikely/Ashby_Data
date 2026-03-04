# 03_VERIFY.md

## Raw Receipt Source
- See `06_TESTS.txt` for wrapper-captured raw command receipts.

## Verification Command
- CMD: `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_observability_api_middleware.py tests/test_ui_event_endpoint_logging.py`
- RESULT: `4 passed, 10 warnings in 0.61s`
- RC: `0`

## Assertions Verified
- Middleware emits `api.request_received` and `api.response_sent` with correlation continuity and duration.
- Backend exception path emits `api.error` and `alert.backend_exception`.
- Startup emits `system.start` under telemetry-on mode.
- `/api/ui/event` emits UI events and routes alerts for `ui.error` and `ui.fetch_failed`.

OVERALL: PASS
