# QUEST_053 — Prequest

Date: 2026-02-07

## Canon / starting state
- Canon source: `Ashby_CANON_2026-02-07_v4.zip` extracted to `/mnt/data/Ashby_Data` + `/mnt/data/Ashby_Engine`.
- Existing state:
  - `evidence_map.json` was **v1** and emitted a single transcript claim with minimal anchors.
  - `minutes.json` and `journal.json` already carried **citations** referencing `segment_id`.

## Requirements (from quest)
- Keep artifact name stable: `artifacts/evidence_map.json`.
- Put version inside the file (v2).
- Builder must support both **meeting** and **journal** runs.
- Must run real tests: `python3 -m pytest -q`.

## Plan
1. Define a v2 evidence_map schema that includes claim objects + anchor objects.
2. Update builder to:
   - Load transcript segments (aligned transcript when present)
   - Extract claims from minutes/journal JSON
   - Convert citations to anchors with timestamps + speaker label
3. Update tests that assert evidence_map version.
4. Run full pytest suite.
