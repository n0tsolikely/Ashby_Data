# Pre-Execution Request

Quest: QUEST_114
Scope: TranscriptVersion artifact schema + runtime store only.

Plan:
1) Add TranscriptVersion schema + validation.
2) Add runtime storage module:
   - ensure_transcripts_dirs
   - create_transcript_version
   - list_transcript_versions
   - load_transcript_version
   - resolve_transcript_version
3) Add focused tests for schema + store behavior.
4) Run targeted pytest + full pytest gate.

Risk controls:
- Keep implementation isolated to meetings module and tests.
- Preserve immutability via write-once artifact writes.
- Enforce safe STUART_ROOT-relative audio_ref paths.
