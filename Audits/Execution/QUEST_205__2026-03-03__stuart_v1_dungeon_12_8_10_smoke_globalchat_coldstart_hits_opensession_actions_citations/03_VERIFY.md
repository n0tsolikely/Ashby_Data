# 03_VERIFY.md

OVERALL: PASS

## Verification Summary
- Executed smoke script through phase 8 with mini fixtures.
- Verified global chat cold-start call (`/api/chat/global`) from `ui={}` with transcript-derived token.
- Asserted response contract:
  - `ok=true`, `scope=global`
  - at least one `hit`
  - at least one `open_session` action
  - citation anchor includes `session_id`, `segment_id`, `t_start`, `t_end`

## Receipt Anchors
- Smoke log: `/home/notsolikely/Ashby_Engine/docs/smoke_outputs/2026-03-04/run.log`
- Global chat request: `/tmp/d12_chat_global_request.json`
- Global chat response: `/tmp/d12_chat_global.json`
- Wrapper receipts: `06_TESTS.txt`
