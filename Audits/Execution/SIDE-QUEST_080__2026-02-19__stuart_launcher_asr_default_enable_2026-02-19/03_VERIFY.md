# 03_VERIFY — SIDE-QUEST_080

Commands run:
1) `bash -n /home/notsolikely/Ashby_Engine/Stuart && echo OK`
   - Result: `OK`

2) `env | rg '^ASHBY_ASR_' || true`
   - Result before launcher defaults: no ASR env vars preset.

3) Runtime evidence check (pre-change behavior diagnosis):
   - Read `/home/notsolikely/ashby_runtime/stuart/runs/run_01KHV81C8P5JBVC7S62KTXV57F/run.json`
   - Observed transcript artifact engine was `stub`.

4) Dependency sanity check for real-engine availability:
   - `STUART_ROOT=/tmp/stuart_runtime python scripts/stuart_preflight.py --strict --json`
   - Result: `ok: true` with faster_whisper, torch, pyannote imports passing.

Conclusion:
- Root cause was launcher/env gating, not missing dependencies.
- Launcher default now routes standard `Stuart` usage to real ASR unless user overrides.
