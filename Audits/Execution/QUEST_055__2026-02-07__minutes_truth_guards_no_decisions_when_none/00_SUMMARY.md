# QUEST_055 — Minutes truth guards (no decisions/actions when none exist)

Date: 2026-02-07

## What changed
- **Minutes renderer now emits explicit truth statements** when no decisions or no action items exist:
  - `No explicit decisions recorded.`
  - `No action items recorded.`

- **Schema tests extended** to explicitly assert that **decisions** and **action_items** require non-empty citations (same truth guard already enforced in schema).

- **Added a renderer regression test** to assert the new empty-section wording appears in `minutes.md`.

## Why
Codex truth-discipline: minutes should never imply decisions/actions exist when the transcript contains none. Silence/empty headings are ambiguous; explicit statements are truthful and stable.

## Files touched
- `Ashby_Engine/ashby/modules/meetings/render/minutes_md.py`
- `Ashby_Engine/tests/test_meetings_minutes_schema_v1.py`
- `Ashby_Engine/tests/test_meetings_minutes_truth_guards_empty_sections.py` (new)

## Verification
- `python3 -m pytest -q` → **77 passed** (see 03_VERIFY.md)
