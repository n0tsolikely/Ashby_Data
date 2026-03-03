# QUEST_053 — evidence_map v2 schema + builder (claim-level anchors)

Date: 2026-02-07

## Goal
Upgrade `artifacts/evidence_map.json` to **v2** so it ties **minutes/journal claims** back to **transcript anchors** at the claim level.

## What shipped
- Added a v2 machine-contract schema + validator for `evidence_map.json`.
- Reworked the evidence map builder so it:
  - Reads `minutes.json` (meeting) or `journal.json` (journal)
  - Extracts claim objects per item (topic/decision/action/etc)
  - Resolves citations to transcript segment anchors (segment_id + t_start/t_end + speaker_label)
  - Writes `artifacts/evidence_map.json` with `version: 2`.
- Updated tests that asserted evidence_map v1 to expect v2.

## Files changed
Engine:
- `ashby/modules/meetings/render/evidence_map.py` (v1 → v2 builder)
- `ashby/modules/meetings/schemas/evidence_map_v2.py` (NEW)

Tests:
- `tests/test_meetings_evidence_map_anchors.py`
- `tests/test_meetings_render_md_pdf_evidence.py`
- `tests/test_meetings_render_journal_md_pdf_evidence.py`

Data:
- Quest moved: `Quest Board/Accepted → Quest Board/Completed`
- This audit bundle updated.
