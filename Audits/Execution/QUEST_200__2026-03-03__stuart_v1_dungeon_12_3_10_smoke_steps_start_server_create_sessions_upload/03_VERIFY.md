# 03_VERIFY.md

## Verification Commands
- `cd /home/notsolikely/Ashby_Engine && bash -n scripts/full_system_smoke_test.sh`
- `STUART_SMOKE_AUTOSTART_BACKEND=1 bash scripts/full_system_smoke_test.sh`
- `rg -n 'QUEST_200|phases 1-3|pending' docs/full_system_smoke_test.md`
- `test -f docs/smoke_outputs/<YYYY-MM-DD>/run.log`

## Raw Receipt Reference
- Full command receipts are stored in `06_TESTS.txt`.

## Verification Summary
- Script syntax valid.
- Phase 1 passed: backend autostart + API reachability.
- Phase 2 passed: meeting and journal sessions created (session IDs logged).
- Phase 3 passed: both fixture uploads succeeded.
- Output log path generated under `docs/smoke_outputs/<date>/run.log`.

## OVERALL
OVERALL: PASS
