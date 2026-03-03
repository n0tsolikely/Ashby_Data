# 02_EXECUTION.md

Implemented:
- `ashby/interfaces/web/templates_api.py` routes:
  - GET `/api/templates`
  - GET `/api/templates/{template_id}`
  - GET `/api/templates/{template_id}/versions`
  - POST `/api/templates/draft`
  - POST `/api/templates`
  - DELETE `/api/templates/{template_id}` (confirm=true required)
- `ashby/interfaces/web/templates_models_v1.py` model contracts.
- `ashby/interfaces/web/app.py` now includes templates router.
- `ashby/interfaces/web/registry_api.py` now emits descriptor objects in `templates_by_mode`.
