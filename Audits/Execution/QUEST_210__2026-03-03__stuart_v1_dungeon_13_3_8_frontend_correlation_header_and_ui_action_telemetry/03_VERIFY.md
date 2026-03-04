# 03_VERIFY.md

## Raw Receipt Source
- See `06_TESTS.txt` for wrapper-captured raw command receipts.

## Verification Command
- CMD: `cd /home/notsolikely/Ashby_Engine/webapp/stuart_frontend/stuart_app && npx eslint src/api/stuartClient.js src/pages/Stuart.jsx --quiet`
- RC: `0`

## Assertions Verified
- `X-Correlation-Id` is now attached by the shared API request wrapper.
- UI telemetry helper emits to `/api/ui/event` using a correlation id.
- Required UI actions are emitted:
  - `ui.click_run`
  - `ui.upload_started`
  - `ui.upload_finished`
  - `ui.chat_send`
  - `ui.export_clicked`
  - `ui.session_loaded`
- Data minimization implemented:
  - chat telemetry uses `text_len` + `text_sha256` + `prefix_len=0`
  - upload telemetry uses `filename` + `size_bytes`

OVERALL: PASS
