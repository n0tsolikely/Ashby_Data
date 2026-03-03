# QUEST_054 — Execution

## 1) Implement shared citation token formatter
Created:
- `Ashby_Engine/ashby/modules/meetings/render/citations.py`

Key behaviors:
- Loads transcript segments (prefers `aligned_transcript.json` for meeting mode, else `transcript.json`).
- Formats stable tokens as:
  - `[S{segment_id}@HH:MM:SS–HH:MM:SS]`
- Uses floor for start seconds and ceil-ish for end seconds to avoid zero-length ranges.

## 2) Update markdown renderers to use the formatter
Updated:
- `Ashby_Engine/ashby/modules/meetings/render/minutes_md.py`
- `Ashby_Engine/ashby/modules/meetings/render/journal_md.py`

Changes:
- Removed local `_fmt_citations()` and per-file segment-id-only formatting.
- Added `segs_by_id = load_segments_by_id(...)` and called `format_citations(..., segs_by_id=...)`.

## 3) Update deterministic render tests
Updated:
- `Ashby_Engine/tests/test_meetings_render_minutes_journal_md_deterministic.py`

Changes:
- Added minimal `transcript.json` writer so timestamp formatting is testable.
- Updated assertions from `【seg:0】` to `[S0@00:00:00–00:00:01]`.

