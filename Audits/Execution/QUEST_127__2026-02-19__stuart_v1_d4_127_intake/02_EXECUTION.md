# Execution

## Changes Applied
ashby/modules/meetings/session_state.py
ashby/modules/meetings/transcript_versions.py
ashby/modules/meetings/pipeline/job_runner.py
ashby/modules/meetings/primary_outputs.py
ashby/modules/meetings/formalize/minutes_json.py
ashby/modules/meetings/formalize/journal_json.py
ashby/modules/meetings/render/evidence_map.py
ashby/modules/meetings/export/bundle.py
ashby/interfaces/web/app.py
ashby/interfaces/web/api_models_v1.py
webapp/stuart_frontend/stuart_app/src/pages/Stuart.jsx
webapp/stuart_frontend/stuart_app/src/api/stuartClient.js
docs/stuart/transcript_versioning_model_v1.md
tests/test_meetings_transcript_versions_api_v1.py
tests/test_meetings_web_api_contract_minimum_v1.py
tests/test_meetings_export_bundle_export_type_filters.py

## Command(s)

a) Targeted validation run:
`cd /home/notsolikely/Ashby_Engine && python -m pytest -q -p no:cacheprovider tests/test_meetings_router_plan.py tests/test_meetings_run_params_validation.py tests/test_meetings_web_api_contract_minimum_v1.py tests/test_meetings_export_bundle_export_type_filters.py tests/test_meetings_transcript_versions_store.py tests/test_meetings_transcript_versions_api_v1.py`
