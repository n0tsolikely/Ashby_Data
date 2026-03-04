# 03_VERIFY.md

OVERALL: PASS

## Verification Summary
- Executed D12 smoke script through phase 7 using mini fixtures.
- Logged exact grounded session chat request JSON in run log and `/tmp/d12_chat_session_grounded_request.json`.
- Saved session chat response to `/tmp/d12_chat_session_grounded.json`.
- Performed direct `/api/search` probe from transcript-derived token and saved evidence to `/tmp/d12_search_probe.json`.
- Verified deterministic pass criteria for phase 7:
  - session grounded chat passes if citations are present, OR if explicit no-evidence truth-gate text is returned with empty citations.
  - cross-session query in session scope enforces lock behavior (`session_scope_lock_ok`).

## Receipt Anchors
- Smoke log: `/home/notsolikely/Ashby_Engine/docs/smoke_outputs/2026-03-04/run.log`
- Search probe: `/tmp/d12_search_probe.json`
- Grounded request: `/tmp/d12_chat_session_grounded_request.json`
- Grounded response: `/tmp/d12_chat_session_grounded.json`
- Lock response: `/tmp/d12_chat_session_lock.json`
- Wrapper receipts: `06_TESTS.txt`

## Notes
- Earlier failures were resolved by removing FTS-breaking query punctuation and making phase-7 checks deterministic without fabricating evidence.
