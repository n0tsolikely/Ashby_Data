# Verification

- Test command executed:
`cd /home/notsolikely/Ashby_Engine && python -m pytest -q -p no:cacheprovider tests/test_meetings_router_plan.py tests/test_meetings_run_params_validation.py tests/test_meetings_web_api_contract_minimum_v1.py tests/test_meetings_export_bundle_export_type_filters.py tests/test_meetings_transcript_versions_store.py tests/test_meetings_transcript_versions_api_v1.py`
- Result: 19 passed in 1.27s
- Scope checks: transcript selection provenance is carried in run artifacts and formalization outputs; export filters include transcript lineage files for formalization/transcript modes.

- Full meetings suite command executed:
`cd /home/notsolikely/Ashby_Engine && timeout 600 python -m pytest -q -p no:cacheprovider tests/test_meetings_* | tee /tmp/meetings_fullsuite_2026-02-19.txt`
- Full meetings suite result: exit_code=0; output stream contained only dot progress (no failures emitted)
- Full meetings suite log: /tmp/meetings_fullsuite_2026-02-19.txt
