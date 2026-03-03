# 02_EXECUTION.md

Commands:
- `PYTHONPATH=/home/notsolikely/Ashby_Engine python -m pytest -q tests/test_llm_gateway_api.py tests/test_meetings_formalize_minutes_json_profile_gated.py tests/test_meetings_formalize_journal_json_profile_gated.py`

Files added:
- `ashby/interfaces/llm_gateway/__init__.py`
- `ashby/interfaces/llm_gateway/app.py`
- `ashby/interfaces/llm_gateway/schemas.py`
- `ashby/interfaces/llm_gateway/validate.py`
- `ashby/interfaces/llm_gateway/providers/__init__.py`
- `ashby/interfaces/llm_gateway/providers/gemini.py`
- `tests/test_llm_gateway_api.py`
