# SIDE-QUEST_077 — Verification

## Smoke gate + truth gate integration
Command:
```bash
cd /mnt/data/Ashby_Engine
python -m pytest -q \
  tests/test_meetings_cli_stuart.py::test_cli_upload_run_status \
  tests/test_meetings_web_door_scaffold.py::test_web_registry_exposes_modes_and_templates \
  tests/test_meetings_web_upload_run.py::test_web_upload_and_run \
  tests/test_telegram_stuart_door_core.py \
  tests/test_meetings_truth_gate_integration.py
```

Result:
```text
/opt/pyvenv/lib/python3.11/site-packages/ddtrace/vendor/psutil/_pslinux.py:527: RuntimeWarning: 'sin' and 'sout' swap memory stats couldn't be determined and were set to 0 ([Errno 2] No such file or directory: '/proc/vmstat')
  warnings.warn(msg, RuntimeWarning)
........                                                                 [100%]
=============================== warnings summary ===============================
../../../opt/pyvenv/lib/python3.11/site-packages/ddtrace/internal/module.py:220
  /opt/pyvenv/lib/python3.11/site-packages/ddtrace/internal/module.py:220: PendingDeprecationWarning: Please use `import python_multipart` instead.
    self.loader.exec_module(module)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 1 warning in 10.37s
```
