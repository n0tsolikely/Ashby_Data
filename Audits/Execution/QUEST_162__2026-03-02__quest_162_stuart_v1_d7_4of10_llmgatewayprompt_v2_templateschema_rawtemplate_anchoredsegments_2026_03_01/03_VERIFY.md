# 03_VERIFY.md
OVERALL: PASS

## Verification
- Gemini prompt builder now consumes template schema and raw template text when present.
- Prompt prefers structured transcript segments over legacy transcript text.
- Prompt includes explicit citation rails and no-invention instruction tied to provided segment IDs.

## Test Evidence
- Wrapped command in `06_TESTS.txt`:
  - `source /home/notsolikely/venvs/ashby-env/bin/activate && cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_llm_gateway_contract_minimum.py tests/test_llm_gateway_api.py`
- Result: `11 passed in 0.45s` (RC 0)
