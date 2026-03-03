# Execution

## 1) Web door `/api/upload` returns plan preview and never runs
File: `Ashby_Engine/ashby/interfaces/web/app.py`

Changes:
- Expanded `/api/upload` signature to allow:
  - `session_id` (optional)
  - `mode` (optional; used when creating a new session)
  - `title` (optional; passed to session creation)
- If `session_id` is omitted:
  - Validate mode via `validate_mode()`
  - Create a new session
- Store upload as contribution via:
  - `store_upload()` (multipart)
  - `store_upload_bytes()` (raw bytes)
- Build plan preview via `clarify_or_preview(text="formalize", ...)` and return it in `plan_preview`
- Explicitly **no call** to `create_run()` or `run_job()` from upload path

## 2) Align legacy scaffold webapp `/upload`
File: `Ashby_Engine/webapp/main.py`

Changes:
- Removed the auto-run behavior from upload.
- `/upload` now:
  - validates mode
  - creates a new session
  - stores contribution
  - returns `plan_preview`

## 3) Minimal UI copy alignment
File: `Ashby_Engine/webapp/static/js/app.js`

Changes:
- Updated the scaffold UI text so it no longer claims "upload runs Stuart and returns a PDF".
- Displays plan preview steps when present.

## 4) Add regression test (the rail)
File: `Ashby_Engine/tests/test_meetings_web_upload_preview_no_run.py`

Adds a focused test that asserts:
- upload returns a `plan_preview` with defaults applied
- upload does **not** create any runs
- upload supports implicit session creation when `session_id` is omitted

## Patch
See `05_DIFF.patch`.
