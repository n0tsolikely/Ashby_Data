# 02_EXECUTION — QUEST_034

Engine changes
- Added: /mnt/data/Ashby_Engine/ashby/modules/meetings/pipeline/normalize.py
- Modified: /mnt/data/Ashby_Engine/ashby/modules/meetings/adapters/adapter_matrix.py (adds normalize adapter)
- Modified: /mnt/data/Ashby_Engine/ashby/modules/meetings/pipeline/job_runner.py (calls normalize and records artifact normalized_audio)
- Modified: /mnt/data/Ashby_Engine/tests/test_execution_profile_and_adapter_matrix.py (assert normalize callable)
- Added: /mnt/data/Ashby_Engine/tests/test_meetings_normalize_ffmpeg.py

Diff captured in this audit via before/after snapshots (see 91_BEFORE if present) + receipts.
