# 03_VERIFY.md

- Verification level: TL2 unit/API + frontend lint
- Commands:
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_chat_new_template_command_returns_draft_action.py`
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_meetings_chat_commands_parse.py tests/test_meetings_chat_commands_sessions_open.py tests/test_meetings_chat_schema_contract.py`
  - `cd /home/notsolikely/Ashby_Engine/webapp/stuart_frontend/stuart_app && npx eslint src/components/stuart/ChatInterface.jsx src/pages/Stuart.jsx --quiet`
- Results:
  - `1 passed in 0.20s`
  - `8 passed in 0.18s`
  - `RC: 0`
- Raw receipts: `06_TESTS.txt`

OVERALL: PASS
