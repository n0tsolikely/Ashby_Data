# 04_OUTCOME.md

QUEST_170 UI scope is implemented.

What is now true:
- Run controls include `Formalization Title (optional)` input.
- Run submission sends `ui.formalization_title` when present.
- Formalization cards display title from backend.
- Formalization cards support inline rename and persist via `PATCH /api/runs/{run_id}`.
- API client now supports `stuartClient.runs.update(runId, payload)`.

Files touched:
- `webapp/stuart_frontend/stuart_app/src/components/stuart/RunControls.jsx`
- `webapp/stuart_frontend/stuart_app/src/components/stuart/FormalizationOutput.jsx`
- `webapp/stuart_frontend/stuart_app/src/pages/Stuart.jsx`
- `webapp/stuart_frontend/stuart_app/src/api/stuartClient.js`

STATUS: PASS
