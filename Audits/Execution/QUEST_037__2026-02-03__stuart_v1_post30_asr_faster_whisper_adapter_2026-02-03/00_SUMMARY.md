# 00_SUMMARY — QUEST_037 (ASR faster-whisper LOCAL_ONLY)

Status: COMPLETED (PASS)
Date (local): 2026-02-03

What changed
- Added transcribe_faster_whisper_or_stub adapter.
- Adapter writes transcript.txt + transcript.json (v1) write-once.
- Auto-ingest into SQLite FTS for formalize runs and write fts_ingest.json receipt.

Receipts
- 12_TEST_OUTPUT__pytest.txt
- 12_TEST_OUTPUT__smoke.txt
