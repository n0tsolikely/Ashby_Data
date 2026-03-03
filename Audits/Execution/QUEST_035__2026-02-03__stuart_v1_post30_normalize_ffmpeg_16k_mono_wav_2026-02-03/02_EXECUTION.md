# 02_EXECUTION — QUEST_035

Engine changes
- Added: /mnt/data/Ashby_Engine/ashby/modules/meetings/adapters/diarize_pyannote.py
- Modified: /mnt/data/Ashby_Engine/ashby/modules/meetings/adapters/adapter_matrix.py (diarize -> diarize_pyannote adapter)
- Added/Updated: /mnt/data/Ashby_Engine/tests/test_meetings_diarize_pyannote_guarded.py

Truth behavior
- If pyannote + HF_TOKEN available: attempt real diarization.
- Else: write stub payload with explicit warning (engine="stub") — not silent success.
