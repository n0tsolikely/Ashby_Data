# 01_PREQUEST — Preconditions

Date: 2026-02-08

## Starting state
- `sqlite_fts.search()` returned `session_id/run_id/segment_id` + `t_start/t_end` fields, but:
  - could **not** filter by mode (meeting/journal)
  - selected `t_start/t_end` only from the FTS row (not the canonical segments table)
- `pipeline/search.py` already wrote `artifacts/search_results.json`, but:
  - did not record scope (session/mode filter) in the payload
- `schemas/search.py` citation anchors were still labeled `kind: transcript_line` (stale)
- Plan builder did not include a mode filter parameter in the SEARCH step

## Dependencies already satisfied
- QUEST_056 (schema v2 anchors)
- QUEST_057 (ingest transcript.json/aligned_transcript.json)

## Constraints
- No UI work (Dungeon 5)
- No refactors beyond minimal wiring to support filters + consistent citation fields

