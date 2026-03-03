# QUEST_060 — Outcome

## Completion criteria
- [x] Attendee query returns sessions where mapped name appears
- [x] No false positives when no mapping exists
- [x] `python3 -m pytest -q` passes

## Notes
- This is **overlay-grounded only**: the query uses `speaker_maps` rows and does not fall back to transcript text.
- Identity resolution across sessions remains out of scope; the mapping is whatever the user set per session.
