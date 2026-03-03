# QUEST_074 — Stuart v1 Export Bundle (session zip) — Summary

## Goal
Implement a deterministic, read-only export bundle zip for Stuart sessions/runs containing:
- run manifest (`run.json`) + session/contribution metadata
- artifacts (e.g., transcript, minutes/journal JSON/MD, evidence_map.json)
- exports (e.g., `minutes.pdf` / `journal.pdf`)

## What changed
### Engine
- **Session bundle now includes per-run `exports/` and `inputs/`**
  - Fixes the missing-PDF issue because PDFs live under `runs/<run_id>/exports/`.
- **Added run-level bundler** (`export_run_bundle`) to create a deterministic zip for a single run.
- **Export result struct** (`ExportBundleResult`) now supports optional `run_id` (only present for run bundles).
- **Export package surface** now exports both `export_session_bundle` and `export_run_bundle`.

### Tests
- Updated CLI export test fixture to create a PDF under `runs/<run_id>/exports/` and assert it is present in the bundle.
- Added a deterministic-output test that creates two bundles and asserts the zip bytes are identical.

## Determinism rails
- Stable ordering (sorted arcnames)
- Normalized zip timestamps (`2000-01-01 00:00:00`)
- Normalized file perms (`0644`)

## Verification
- `python3 -m pytest -q tests/test_meetings_cli_search_export.py`
  - Result: **3 passed**
