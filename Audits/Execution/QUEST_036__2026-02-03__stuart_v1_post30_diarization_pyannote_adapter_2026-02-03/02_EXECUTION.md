# 02_EXECUTION — QUEST_036

Engine changes
- Modified: /mnt/data/Ashby_Engine/ashby/modules/meetings/pipeline/job_runner.py
  - Meeting mode: diarize (real/stub)
  - Journal mode: skip diarization by default
  - Speaker hint support (2/3+) via write-once inputs/speaker_hint.json
- Modified: /mnt/data/Ashby_Engine/ashby/modules/meetings/adapters/diarize_pyannote.py
  - Reads speaker_hint.json and passes hint to pyannote pipeline best-effort
  - Includes speaker_hint in diarization_segments.json payload
- Added: /mnt/data/Ashby_Engine/tests/test_meetings_diarization_policy.py
  - Asserts journal mode skips diarization
  - Asserts speaker_hint receipt exists and payload includes speaker_hint

Truth / token gating
- No secrets hardcoded.
- If pyannote missing or HF_TOKEN missing, adapter writes stub payload with explicit warning (engine='stub').
