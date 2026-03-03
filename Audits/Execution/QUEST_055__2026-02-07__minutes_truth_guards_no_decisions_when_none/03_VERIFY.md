# 03_VERIFY — Tests / receipts

Quest: QUEST_055
Date: 2026-02-07

## Targeted regression tests
Command:
```bash
cd /mnt/data/Ashby_Engine
PYTHONPATH=/mnt/data/Ashby_Engine pytest -q \
  tests/test_meetings_minutes_schema_v1.py \
  tests/test_meetings_minutes_truth_guards_empty_sections.py
```
Result:
```
5 passed in 0.59s
```

## Full suite (quest requirement)
Command:
```bash
cd /mnt/data/Ashby_Engine
PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q
```
Receipt (tail of output):
```
=============================== warnings summary ===============================
../../../opt/pyvenv/lib/python3.11/site-packages/ddtrace/internal/module.py:220
  /opt/pyvenv/lib/python3.11/site-packages/ddtrace/internal/module.py:220: PendingDeprecationWarning: Please use `import python_multipart` instead.
    self.loader.exec_module(module)

tests/test_meetings_web_door_scaffold.py::test_index_has_mode_placeholder_and_no_default_selected
  /opt/pyvenv/lib/python3.11/site-packages/starlette/templating.py:178: DeprecationWarning: The `name` is not the first parameter anymore. The first parameter should be the `Request` instance.
  Replace `TemplateResponse(name, {"request": request})` by `TemplateResponse(request, name)`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
77 passed, 2 warnings in 47.08s
```
