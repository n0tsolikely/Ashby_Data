# 04_OUTCOME.md

QUEST_171 is implemented and verified.

What is now true:
- `GET /api/sessions/{session_id}/export` supports `export_type=dev_bundle`.
- API accepts and validates:
  - `transcript_formats` (allowed: `txt,md,pdf`)
  - `formalization_formats` (allowed: `md,pdf`)
- Invalid format values return `400 INVALID_REQUEST`.
- API response now includes deterministic traceable `zip.download_name` containing `session_id` and sanitized session title (if present).
- Export builder function signature now accepts format-selection inputs (reserved for D8 builder v2 use in QUEST_172).

Files touched:
- `ashby/interfaces/web/app.py`
- `ashby/modules/meetings/export/bundle.py`
- `tests/test_export_api_v2_params.py`

STATUS: PASS
