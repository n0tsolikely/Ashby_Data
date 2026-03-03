# 02_EXECUTION.md

Key implementation details:
- `GeminiProvider.__init__` fails when `GEMINI_API_KEY` is missing
- provider model configurable via `GEMINI_MODEL`
- provider call path isolated in `ashby/interfaces/llm_gateway/providers/gemini.py`
