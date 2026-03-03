# 02_EXECUTION.md

Implemented:
- `formalize/minutes_json.py` and `formalize/journal_json.py`:
  - `_apply_output_metadata` now writes `template_title`.
  - formalize functions accept optional `template_version` and load exact version via registry.
- `pipeline/job_runner.py`:
  - resolves template spec before formalization/extract-only and records `resolved_template` artifact with id/version/title.
  - passes locked `template_version` into formalize generators.
- `export/bundle.py`:
  - dev bundle now attempts to capture exact template internals under:
    - `dev/templates/<run_id>/<template_id>/v<version>/metadata.json`
    - `dev/templates/<run_id>/<template_id>/v<version>/template.md`
