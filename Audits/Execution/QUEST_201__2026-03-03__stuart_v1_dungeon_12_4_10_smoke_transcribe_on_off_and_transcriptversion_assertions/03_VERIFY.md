# 03_VERIFY.md

## Verification Commands
- `cd /home/notsolikely/Ashby_Engine && bash -n scripts/full_system_smoke_test.sh`
- `STUART_SMOKE_USE_MINI_FIXTURES=1 ASHBY_ASR_ENABLE=0 STUART_SMOKE_AUTOSTART_BACKEND=1 STUART_SMOKE_RUN_TIMEOUT_SEC=300 bash scripts/full_system_smoke_test.sh`
- `rg -n 'QUEST_201|Transcribe meeting fixture|transcript version count' docs/full_system_smoke_test.md`
- `test -f /tmp/d12_transcripts_meeting.json`

## Raw Receipt Reference
- Full raw command output is recorded in `06_TESTS.txt`.

## Verification Summary
- Script reached phase 4 and submitted both transcribe runs.
- Both run IDs reached terminal `succeeded`.
- Transcript versions for meeting session counted at `2`.
- Details captured in `/tmp/d12_transcripts_meeting.json`.

## OVERALL
OVERALL: PASS
