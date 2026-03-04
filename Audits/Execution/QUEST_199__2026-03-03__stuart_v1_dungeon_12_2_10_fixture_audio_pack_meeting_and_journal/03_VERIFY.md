# 03_VERIFY.md

## Verification Commands
- `cd /home/notsolikely/Ashby_Engine && python3 - << 'PY' ...` (manifest parse + wave duration checks)
- `bash -n scripts/full_system_smoke_test.sh`
- `rg -n 'stuart_smoke|fixture' scripts/full_system_smoke_test.sh docs/full_system_smoke_test.md tests/fixtures/stuart_smoke/README.md`

## Raw Receipt Reference
- Full raw receipts are in `06_TESTS.txt`.

## Verification Summary
- `fixture_manifest.json` is valid JSON.
- Meeting fixture duration verified at ~36.0s.
- Journal fixture duration verified at ~42.0s.
- Smoke script and docs reference canonical fixture paths.

## OVERALL
OVERALL: PASS
