# QUEST_062 — webapp_upload_stores_contribution_not_run

Date: 2026-02-09

## What changed
We added a hard privacy rail to the web upload entrypoints: **Upload ≠ Process**.

- `ashby/interfaces/web` `/api/upload` now:
  - Stores the upload as a **contribution** (immutable)
  - (Optionally) creates a **session** when `session_id` is omitted
  - Returns a deterministic **plan preview** using defaults (`template=default`, `retention=MED`, `speakers=<mode default>`)
  - **Does not** create a run or trigger `job_runner`

- Legacy scaffold `webapp/main.py` `/upload` was aligned to the same behavior (no auto-run).

## Why
This is the consent / privacy gate requirement for Stuart D5: uploading media must not automatically transcribe/process.

## Files changed
- `Ashby_Engine/ashby/interfaces/web/app.py`
- `Ashby_Engine/webapp/main.py`
- `Ashby_Engine/webapp/static/js/app.js`
- `Ashby_Engine/tests/test_meetings_web_upload_preview_no_run.py` (new)

## Tests
- `python3 -m pytest -q` (PASS, exit 0)

Artifacts:
- `05_DIFF.patch`
- `06_PYTEST_-q.txt`
