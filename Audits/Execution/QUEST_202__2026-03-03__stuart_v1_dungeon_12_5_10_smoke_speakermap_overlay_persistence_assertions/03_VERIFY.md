# 03_VERIFY.md

## Verification Commands
- `cd /home/notsolikely/Ashby_Engine && bash -n scripts/full_system_smoke_test.sh`
- `STUART_SMOKE_USE_MINI_FIXTURES=1 ASHBY_ASR_ENABLE=0 STUART_SMOKE_AUTOSTART_BACKEND=1 STUART_SMOKE_RUN_TIMEOUT_SEC=300 bash scripts/full_system_smoke_test.sh`
- `rg -n 'QUEST_202|speaker map overlay|assert overlay persistence' docs/full_system_smoke_test.md`
- `test -f /tmp/d12_speaker_map_get.json`

## Raw Receipt Reference
- Full raw command receipt is in `06_TESTS.txt`.

## Verification Summary
- Script executed phases 1-5 successfully.
- Both transcribe runs succeeded.
- Speaker map PUT + GET roundtrip passed on diarized transcript version.
- Persistence proof captured in `/tmp/d12_speaker_map_get.json`.

## OVERALL
OVERALL: PASS
