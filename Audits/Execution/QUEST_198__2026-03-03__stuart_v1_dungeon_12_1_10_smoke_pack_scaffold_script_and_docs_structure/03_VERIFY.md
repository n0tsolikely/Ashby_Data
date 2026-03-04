# 03_VERIFY.md

## Verification Commands
- `cd /home/notsolikely/Ashby_Engine && chmod +x scripts/full_system_smoke_test.sh && bash -n scripts/full_system_smoke_test.sh && rg -n 'PHASE|D12|smoke_outputs' scripts/full_system_smoke_test.sh docs/full_system_smoke_test.md`

## Raw Receipt Reference
- Full raw command receipt is in `06_TESTS.txt`.

## Command Output (summary)
- `bash -n` returned RC `0`.
- `rg` confirmed D12 phase headers and output path contract in:
  - `scripts/full_system_smoke_test.sh`
  - `docs/full_system_smoke_test.md`

## PASS/FAIL/BLOCKED
- PASS: scaffold script exists, is executable, shell-valid, and prints ordered phase labels.
- PASS: doc exists and mirrors script phases with smoke_outputs contract.
- FAIL: any missing script/doc path or phase labels.
- BLOCKED: none.

## OVERALL
OVERALL: PASS
