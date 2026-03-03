# QUEST RENNUMBER MAP — Stuart v1 (REV7)
Date: 2026-02-04

Purpose:
- Fix quest numbering drift from REV6.
- Ensure numeric order matches execution dependencies from current engine state.
- Preserve intent of existing quests; only re-ordered/renamed and tightened scopes.
- Pulled JSON→MD renderer quest into the accepted block so the first run of quests is end-to-end coherent.

## Old → New mapping
| Old ID | Old Title (short) | New ID | New Title (short) |
|---:|---|---:|---|
| 046 | Run params: retention/template validation | 042 | Run params: retention/template validation |
| 047 | Default templates: meeting/journal system prompts | 043 | Default templates: meeting/journal system prompts |
| 048 | Minutes JSON schema v1 | 044 | Minutes JSON schema v1 |
| 049 | Journal JSON schema v1 | 045 | Journal JSON schema v1 |
| 050 | LLM formalize meeting → minutes.json | 046 | Formalize meeting → minutes.json (profile-gated) |
| 051 | LLM formalize journal → journal.json | 047 | Formalize journal → journal.json (profile-gated) |
| 052 (board) | Render MD from minutes/journal JSON | 048 | JSON → MD renderers (deterministic) |
| 042 | Output naming: minutes.md / journal.md | 049 | Output naming: minutes.md / journal.md |
| 043 | Output naming: minutes.pdf / journal.pdf | 050 | Output naming: minutes.pdf / journal.pdf |
| 044 | Diarization artifact naming (diarization.json) | 051 | Diarization artifact naming (diarization.json) |
| 045 | Run manifest primary outputs pointers | 052 | Run manifest primary outputs pointers |

## Notes
- New QUEST_046 / QUEST_047 were amended to explicitly support **LOCAL_ONLY** (no remote LLM). Remote LLM is optional and gated by execution profile.
- QUEST_048 scope was tightened to **renderers only**; pipeline wiring happens in QUEST_049/050.
- Evidence/Retrieval/Door/Overlay quests (053–075) were not renumbered.
