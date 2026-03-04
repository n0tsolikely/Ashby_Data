# 03_VERIFY.md

## Raw Receipt Source
- See `06_TESTS.txt` for wrapper-captured raw command receipts.

## Verification Command
- CMD: `cd /home/notsolikely/Ashby_Engine/webapp/stuart_frontend/stuart_app && npx eslint src/api/stuartClient.js src/main.jsx src/pages/Stuart.jsx --quiet`
- RC: `0`

## Assertions Verified
- Global client-side error hooks added:
  - `window.onerror` -> `ui.error`
  - `window.onunhandledrejection` -> `ui.error`
- Shared API wrapper now emits `ui.fetch_failed` for:
  - non-2xx responses
  - thrown fetch exceptions
- Error/failure payloads are redacted/truncated before telemetry emit.
- Telemetry remains best-effort and non-blocking.

OVERALL: PASS
