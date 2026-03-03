# Execution Log

Implemented code artifacts:
- /home/notsolikely/Ashby_Engine/ashby/modules/meetings/transcript_versions.py
- /home/notsolikely/Ashby_Engine/ashby/modules/meetings/schemas/artifacts_v1.py
- /home/notsolikely/Ashby_Engine/tests/test_meetings_transcript_versions_store.py
- /home/notsolikely/Ashby_Engine/tests/test_meetings_artifact_schemas_v1.py

Key implementation points:
- TranscriptVersion payload includes:
  `version`, `transcript_version_id`, `session_id`, `run_id`, `created_ts`,
  `diarization_enabled`, `asr_engine`, `audio_ref`, `segments`.
- Version artifact path:
  `sessions/{session_id}/transcripts/versions/{transcript_version_id}.json`.
- Session index path:
  `sessions/{session_id}/transcripts/index.jsonl`.
- Global lookup path:
  `transcript_versions/lookup.jsonl`.
- Deterministic writes:
  - artifact JSON via `dump_json(..., write_once=True)`
  - JSONL rows via `json.dumps(..., sort_keys=True)`.
- Safety rail:
  absolute `audio_ref.path` must resolve under STUART_ROOT or creation fails.
