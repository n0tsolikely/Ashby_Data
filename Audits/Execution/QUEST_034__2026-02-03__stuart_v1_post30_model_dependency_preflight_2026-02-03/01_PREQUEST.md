# 01_PREQUEST — QUEST_034 (Normalize: ffmpeg → 16kHz mono wav)

Date (local): 2026-02-03

Goal
- Add deterministic normalize stage that produces run_dir/artifacts/normalized.wav (write-once)
- Record artifact kind=normalized_audio
- Use system ffmpeg (LOCAL_ONLY)

PASS
- pytest PASS
- smoke run_job(formalize) produces normalized.wav + artifact kind present
