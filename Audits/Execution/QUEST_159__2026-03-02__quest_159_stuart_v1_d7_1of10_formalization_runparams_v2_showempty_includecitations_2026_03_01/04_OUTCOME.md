# 04_OUTCOME.md

QUEST_ID: QUEST_159
STATUS: COMPLETED_CANDIDATE

What is now true:
- Formalize run contract supports two explicit flags end-to-end in request/planning layer:
  - include_citations (default false)
  - show_empty_sections (default false)
- Frontend RunControls now sends include_citations/show_empty_sections in run payload.
- Router plan formalize step now persists both flags explicitly even when false.
- Store normalization now keeps both flags deterministic on formalize params.

Artifacts changed (engine repo):
- ashby/modules/meetings/schemas/plan.py
- ashby/modules/meetings/schemas/run_request.py
- ashby/modules/meetings/plan_builder.py
- ashby/modules/meetings/store.py
- webapp/stuart_frontend/stuart_app/src/components/stuart/RunControls.jsx
- webapp/stuart_frontend/stuart_app/src/pages/Stuart.jsx
- tests/test_meetings_router_plan.py
- tests/test_meetings_run_params_validation.py

Verification artifact:
- 03_VERIFY.md (OVERALL: PASS)
- 06_TESTS.txt (12 passed, RC=0)
