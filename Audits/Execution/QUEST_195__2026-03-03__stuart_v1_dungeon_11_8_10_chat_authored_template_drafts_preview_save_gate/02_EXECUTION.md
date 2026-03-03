# 02_EXECUTION.md

Implemented:
- `ashby/modules/meetings/schemas/chat.py`: added `ChatActionTemplateDraftV1` and parser/union support.
- `ashby/modules/meetings/chat/commands.py`:
  - help text includes `/new_template <mode> | <title> | <description>`
  - command handler generates deterministic draft action via importer seam.
- Frontend:
  - `ChatInterface.jsx` action button label support for `template_draft`.
  - `Stuart.jsx` action handling to open modal, preview markdown, Save/Cancel, and persist via `stuartClient.templates.create`.
- Test added: `tests/test_chat_new_template_command_returns_draft_action.py`.
