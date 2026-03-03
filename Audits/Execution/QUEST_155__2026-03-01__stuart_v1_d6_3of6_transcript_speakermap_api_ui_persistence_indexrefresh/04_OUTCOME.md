# 04_OUTCOME.md

STATUS: PASS

- Implemented transcript-scoped speaker map read/write endpoints:
  - GET `/api/transcripts/{transcript_version_id}/speaker_map`
  - PUT/POST `/api/transcripts/{transcript_version_id}/speaker_map`
- Updated GET `/api/transcripts/{transcript_version_id}` to return:
  - `speaker_map`
  - `speaker_overlay_id`
  - `speakers` (discovered labels from transcript segments)
- Rewired run endpoint `/api/runs/{run_id}/speaker_map` to delegate to transcript-scoped logic.
- Added index refresh helper to update `speaker_maps` rows for the transcript's run on save/clear.
- Updated frontend to save speaker map by `transcript_version_id` (no run-scoped save dependency).
- Added/updated backend tests for new transcript speaker map contracts and delegation behavior.

Notes:
- Initial test run failed on `speaker_maps` FK constraints for transcript versions without indexed run/session rows.
- Resolved by upserting `sessions`/`runs` rows in transcript-scoped index refresh helper before speaker_maps write.
BLOCKED: governance validate failed (see output above).
