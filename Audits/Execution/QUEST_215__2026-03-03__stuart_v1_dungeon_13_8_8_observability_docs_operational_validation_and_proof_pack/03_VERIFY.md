# 03_VERIFY.md

## Raw Receipt Source
- See `06_TESTS.txt` for wrapper-captured raw command receipts.

## Verification Command
- CMD: `cd /home/notsolikely/Ashby_Engine && mkdir -p docs/smoke_outputs/2026-03-04 && export ASHBY_EVENT_LOGGING=1 && export STUART_ROOT=/home/notsolikely/ashby_runtime/stuart && PYTHONPATH=/home/notsolikely/Ashby_Engine python /tmp/d13_observability_proof.py | tee docs/smoke_outputs/2026-03-04/d13_observability_run.log && python3 tools/realtime_log_doctor.py --stuart-root /home/notsolikely/ashby_runtime/stuart --lines 400 | tee docs/smoke_outputs/2026-03-04/d13_observability_doctor.log && tail -n 80 /home/notsolikely/ashby_runtime/stuart/realtime_log/events.jsonl > docs/smoke_outputs/2026-03-04/d13_events_tail.jsonl && tail -n 80 /home/notsolikely/ashby_runtime/stuart/realtime_log/alerts.jsonl > docs/smoke_outputs/2026-03-04/d13_alerts_tail.jsonl && tail -n 80 /home/notsolikely/ashby_runtime/stuart/realtime_log/ui.jsonl > docs/smoke_outputs/2026-03-04/d13_ui_tail.jsonl && tail -n 80 /home/notsolikely/ashby_runtime/stuart/realtime_log/llm.jsonl > docs/smoke_outputs/2026-03-04/d13_llm_tail.jsonl`
- RC: `0`

## Assertions Verified
- Documentation created for observability enable/tail/doctor workflow.
- Runtime proof logs captured under `docs/smoke_outputs/2026-03-04/`.
- Doctor output demonstrates grouped causal chains by `correlation_id`.
- Proof chain includes UI -> API -> pipeline -> LLM events.

OVERALL: PASS
