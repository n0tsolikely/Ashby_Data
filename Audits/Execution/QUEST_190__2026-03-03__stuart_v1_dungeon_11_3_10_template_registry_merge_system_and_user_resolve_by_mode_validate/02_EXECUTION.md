# 02_EXECUTION.md

Implemented in `template_registry.py`:
- `TemplateDescriptor` and per-mode system/user descriptor collection.
- Dynamic `allowed_templates_for_mode` merge logic with system `default` stability rule.
- `load_template_spec(..., version=...)` support for runtime user templates.
- `validate_template(..., version=...)` version-aware parse validation.
- Added `template_title` to `TemplateSpec`.

Tests added:
- `tests/test_template_registry_merges_system_and_user.py`
