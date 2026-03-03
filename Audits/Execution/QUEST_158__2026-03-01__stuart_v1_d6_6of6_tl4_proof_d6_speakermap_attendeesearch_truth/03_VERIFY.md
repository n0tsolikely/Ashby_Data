# 03_VERIFY.md

OVERALL: PASS

Automated proof rails:
- `pytest -q` focused D6 verification sweep: PASS (`12 passed`).
- Frontend build: PASS.

UI proof artifacts:
- `Ashby_Data/Proofs/D6/d6_transcript_labels.png`
- `Ashby_Data/Proofs/D6/d6_speaker_map_persist.png`
- `Ashby_Data/Proofs/D6/d6_search_badges.png`
- Runtime scenario receipt: `Ashby_Data/Proofs/D6/d6_run_log.txt`

Truth gates verified:
- attendee != transcript mention false positives (covered in tests).
- overlay scope is transcript_version-scoped (covered in tests + API behavior).
- UI label behavior and mapped-name persistence evidenced by screenshots.

Raw execution receipts: `06_TESTS.txt`.
