# 03_VERIFY.md

Quest: SIDE-QUEST_076  
Date: 2026-02-07

## Grep proof: meetings module no longer imports legacy profile module
Command:
```bash
grep -Rni "ashby\.core\.execution_profiles" ashby/modules/meetings --exclude-dir=__pycache__
```

Output:
```text
(no matches)
```

## Grep proof: single ExecutionProfile class definition in core
Command:
```bash
grep -Rni "class ExecutionProfile" ashby/core --exclude-dir=__pycache__
```

Output:
```text
ashby/core/profile.py:10:class ExecutionProfile(str, Enum):
```

## Full test suite
Command:
```bash
PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q
```

Exit code: `0`

Output (verbatim):
```text
/opt/pyvenv/lib/python3.11/site-packages/ddtrace/vendor/psutil/_pslinux.py:527: RuntimeWarning: 'sin' and 'sout' swap memory stats couldn't be determined and were set to 0 ([Errno 2] No such file or directory: '/proc/vmstat')
  warnings.warn(msg, RuntimeWarning)
[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[33m [ 92%]
[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[33m                                                                   [100%][0m
[33m=============================== warnings summary ===============================[0m
../../../opt/pyvenv/lib/python3.11/site-packages/ddtrace/internal/module.py:220
  /opt/pyvenv/lib/python3.11/site-packages/ddtrace/internal/module.py:220: PendingDeprecationWarning: Please use `import python_multipart` instead.
    self.loader.exec_module(module)

tests/test_meetings_web_door_scaffold.py::test_index_has_mode_placeholder_and_no_default_selected
  /opt/pyvenv/lib/python3.11/site-packages/starlette/templating.py:178: DeprecationWarning: The `name` is not the first parameter anymore. The first parameter should be the `Request` instance.
  Replace `TemplateResponse(name, {"request": request})` by `TemplateResponse(request, name)`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m[32m78 passed[0m, [33m[1m2 warnings[0m[33m in 31.06s[0m[0m
```
