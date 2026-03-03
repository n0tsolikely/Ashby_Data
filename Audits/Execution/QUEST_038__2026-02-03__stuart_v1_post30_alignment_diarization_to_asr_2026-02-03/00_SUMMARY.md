# 00_SUMMARY — QUEST_038 (Alignment diarization ↔ ASR)

Status: COMPLETED (PASS)
Date (local): 2026-02-03

What changed
- Added a deterministic, pure algorithmic alignment stage (time overlap) producing:
  - run_dir/artifacts/aligned_transcript.json (version=1, write-once)
- Wired alignment through adapter matrix (routing only) and job_runner (orchestrator only).

Receipts
- pytest PASS: 12_TEST_OUTPUT__pytest.txt
- smoke PASS: 12_TEST_OUTPUT__smoke.txt
- initial smoke failure preserved: 12_TEST_OUTPUT__smoke_FAIL_01.txt
- diff: 10_DIFF.patch
