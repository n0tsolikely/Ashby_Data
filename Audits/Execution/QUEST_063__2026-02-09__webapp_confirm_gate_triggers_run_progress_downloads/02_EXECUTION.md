# EXECUTION — QUEST_063

## 1) Backend: deterministic downloads + progress payload

### `ashby/interfaces/web/runs.py`
- Added `primary_downloads(run_id, state=...)`:
  - Uses `run.json["primary_outputs"]` if present.
  - Falls back to `resolve_primary_outputs(run_id)` if missing.
  - Returns a stable structure with download URLs under `/download/{run_id}/{filename}`.

### `ashby/interfaces/web/app.py`
- `GET /api/runs/{run_id}` now includes:
  - `progress`: `poll_progress(run_id)`
  - `downloads`: `primary_downloads(run_id, state=state)`
  - existing `artifacts` listing preserved
- Added `GET /api/runs/{run_id}/progress` (thin wrapper around `poll_progress`).

## 2) Frontend: show progress + primary outputs

### `ashby/interfaces/web/static/app.js`
- Added a Run Status card that updates on each poll:
  - status / stage / progress
- Added `renderPrimaryDownloads(...)` and made primary outputs first-class.
- Kept an artifacts fallback card for debugging.
- Renamed run button to **“Confirm & Run”**.

## 3) Tests

### `tests/test_meetings_web_upload_run.py`
- Extended the existing E2E web run test to assert:
  - `downloads.primary.pdf` exists
  - its filename matches the basename from `state.primary_outputs.pdf.path`
  - the download URL returns a real PDF response (`%PDF`)

