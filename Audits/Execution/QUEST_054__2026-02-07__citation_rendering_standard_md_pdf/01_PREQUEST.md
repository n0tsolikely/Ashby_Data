# QUEST_054 — Prequest (baseline)

## Baseline behavior (pre-change)
- `minutes.md` and `journal.md` appended citations as `【seg:<id>】` tokens.
- Tokens only contained `segment_id` (no timestamps).
- PDF adapter (WeasyPrint) renders the markdown output as text; citations appeared exactly as written.

## Baseline constraint gap
Quest requires:
- stable identifiers = `segment_id + timestamps`
- consistent token syntax across MD/PDF
- avoid PDF wrapping corruption

Baseline did not satisfy "segment_id + timestamps" requirement.
