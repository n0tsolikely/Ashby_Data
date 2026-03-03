# 00_SUMMARY — QUEST_036 (Stage 1 Diarization: pyannote adapter)

Status: COMPLETED (PASS)
Date (local): 2026-02-03

What is now true
- Meeting mode defaults to diarization (pyannote when available; otherwise stub with explicit warning).
- Journal mode defaults to skipping diarization.
- Optional speaker hint supported (params.speakers / speaker_count / num_speakers):
  - job_runner writes inputs/speaker_hint.json (write-once)
  - diarize_pyannote reads hint and passes it to pyannote best-effort
- diarization_segments.json is canonical v1 and write-once.

Receipts
- pytest PASS: 12_TEST_OUTPUT__pytest.txt
- smoke PASS: 12_TEST_OUTPUT__smoke.txt
