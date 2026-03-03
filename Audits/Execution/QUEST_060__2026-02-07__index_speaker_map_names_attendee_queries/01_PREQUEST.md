# QUEST_060 — Pre-Request

## Canon / Scope rails
- Canon input: `Ashby_CANON_2026-02-08_v12.zip` extracted to:
  - `/mnt/data/Ashby_Data`
  - `/mnt/data/Ashby_Engine`
- Quest file: `/mnt/data/Ashby_Data/Quest Board/Accepted/QUEST_060__Stuart_v1_D4_5of5_Index_Speaker_Map_Names_Attendee_Queries_2026-02-04.txt`

## Constraints (from quest)
- **Never assume** a name mapping unless the user provided a speaker overlay.
- No identity resolution across sessions.

## Intended design
- Add a persistent index table for user-provided speaker mappings.
- Populate it at ingestion time (per run) using the current `active_speaker_overlay_id`.
- Provide a helper query to return sessions by attendee name (case/whitespace-insensitive exact match).
