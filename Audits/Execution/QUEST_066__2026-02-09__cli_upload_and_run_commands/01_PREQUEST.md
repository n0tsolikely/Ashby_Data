# QUEST_066 — Prereqs / Inputs

Date: 2026-02-09

## Canon baseline
- Working directory: `/mnt/data`
- Canon extracted from: `Ashby_CANON_2026-02-09_v22.zip`
- Canon folders (authoritative):
  - `/mnt/data/Ashby_Data`
  - `/mnt/data/Ashby_Engine`

## Dependencies
- QUEST_061 (RunRequest contract) must exist and be in force.
  - This quest consumes `ashby.modules.meetings.schemas.run_request.RunRequest`.

## Governance / rails
- **No heuristics**: CLI must not guess output filenames; it must use run manifest pointers.
- **Confirm rail required**: CLI must never auto-run without explicit confirmation.
- **Real tests required**: verification must be executed in this environment.
