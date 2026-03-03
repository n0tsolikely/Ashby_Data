# 00_SUMMARY — QUEST_034 (Normalize: ffmpeg → 16kHz mono wav)

Status: COMPLETED (PASS)
Date (local): 2026-02-03

- Added normalize stage (ffmpeg) producing artifacts/normalized.wav (write-once).
- Wired normalize through meetings adapter matrix and job_runner.
- Records artifact kind=normalized_audio.

Receipts:
- 12_TEST_OUTPUT__pytest.txt
- 12_TEST_OUTPUT__smoke.txt
