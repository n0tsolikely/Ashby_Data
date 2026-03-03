# 02_EXECUTION.md

Implementation:
- `ashby/interfaces/llm_gateway/validate.py` performs schema checks using:
  - `validate_minutes_v1`
  - `validate_journal_v1`
- app returns `schema_validation_failed` for invalid provider payloads
