# 02_EXECUTION.md

Quest: SIDE-QUEST_076  
Date: 2026-02-07

## Steps performed
1) Made `ashby.core.profile` the canonical API surface by adding:
   - `get_execution_profile()` (reads `ASHBY_EXECUTION_PROFILE`, defaults LOCAL_ONLY, invalid -> LOCAL_ONLY)

2) Converted `ashby.core.execution_profiles` into a deprecated shim:
   - re-exports `ExecutionProfile` and `get_execution_profile` from `ashby.core.profile`
   - contains **no business logic**

3) Updated Meetings module imports to use canonical substrate:
   - replaced `from ashby.core.execution_profiles import ...`
   - with `from ashby.core.profile import ...`

4) Updated unit tests to:
   - import canonical profile
   - assert shim exports **the exact same type/function objects** (no parallel enum)

## Diffs (key)
### `ashby/core/profile.py`
```diff
--- a/Ashby_Engine/ashby/core/profile.py
+++ b/Ashby_Engine/ashby/core/profile.py
@@ -1,4 +1,6 @@
 from __future__ import annotations
+
+import os
 
 from dataclasses import dataclass, field
 from enum import Enum
@@ -18,6 +20,23 @@
     LOCAL_ONLY = "LOCAL_ONLY"
     HYBRID = "HYBRID"
     CLOUD = "CLOUD"
+
+
+
+def get_execution_profile() -> ExecutionProfile:
+    """Return the active execution profile.
+
+    Rule:
+    - Reads ASHBY_EXECUTION_PROFILE from env.
+    - Defaults to LOCAL_ONLY.
+    - Invalid values fall back to LOCAL_ONLY (truthful + safe).
+    """
+    raw = (os.environ.get("ASHBY_EXECUTION_PROFILE") or "").strip().upper()
+    try:
+        return ExecutionProfile(raw) if raw else ExecutionProfile.LOCAL_ONLY
+    except Exception:
+        return ExecutionProfile.LOCAL_ONLY
+
 
 
 DataCategory: TypeAlias = Literal["audio", "transcript", "text", "image", "metadata"]

```

### `ashby/core/execution_profiles.py`
```diff
--- a/Ashby_Engine/ashby/core/execution_profiles.py
+++ b/Ashby_Engine/ashby/core/execution_profiles.py
@@ -1,25 +1,18 @@
 from __future__ import annotations
 
-import os
-from enum import Enum
+"""Deprecated shim module.
 
+This file exists only for backwards compatibility with older imports.
 
-class ExecutionProfile(str, Enum):
-    LOCAL_ONLY = "LOCAL_ONLY"
-    HYBRID = "HYBRID"
-    CLOUD = "CLOUD"
+Canonical execution profile + selection helper live in:
+  ashby.core.profile
 
+Do NOT add new business logic here.
+"""
 
-def get_execution_profile() -> ExecutionProfile:
-    """Return the active execution profile.
+from ashby.core.profile import ExecutionProfile, get_execution_profile
 
-    Rule:
-    - Reads ASHBY_EXECUTION_PROFILE from env.
-    - Defaults to LOCAL_ONLY.
-    - Invalid values fall back to LOCAL_ONLY (truthful + safe).
-    """
-    raw = (os.environ.get("ASHBY_EXECUTION_PROFILE") or "").strip().upper()
-    try:
-        return ExecutionProfile(raw) if raw else ExecutionProfile.LOCAL_ONLY
-    except Exception:
-        return ExecutionProfile.LOCAL_ONLY
+__all__ = [
+    "ExecutionProfile",
+    "get_execution_profile",
+]

```

### Meetings module import updates (representative)
```diff
--- a/Ashby_Engine/ashby/modules/meetings/formalize/minutes_json.py
+++ b/Ashby_Engine/ashby/modules/meetings/formalize/minutes_json.py
@@ -6,7 +6,7 @@
 from pathlib import Path
 from typing import Any, Dict, List, Optional, Set, Tuple
 
-from ashby.core.execution_profiles import ExecutionProfile, get_execution_profile
+from ashby.core.profile import ExecutionProfile, get_execution_profile
 from ashby.modules.meetings.hashing import sha256_file
 from ashby.modules.meetings.schemas.artifacts_v1 import dump_json
 from ashby.modules.meetings.schemas.minutes_v1 import validate_minutes_v1

```

```diff
--- a/Ashby_Engine/ashby/modules/meetings/pipeline/job_runner.py
+++ b/Ashby_Engine/ashby/modules/meetings/pipeline/job_runner.py
@@ -7,7 +7,7 @@
 from typing import Any, Dict, List, Optional
 
 from ashby.modules.meetings.init_root import init_stuart_root
-from ashby.core.execution_profiles import get_execution_profile
+from ashby.core.profile import get_execution_profile
 from ashby.modules.meetings.adapters.adapter_matrix import get_meetings_adapter_matrix
 from ashby.modules.meetings.input_resolver import resolve_input_contribution
 from ashby.modules.meetings.store import get_run_state, update_run_state, sha256_file

```

### Tests
```diff
--- a/Ashby_Engine/tests/test_execution_profile_and_adapter_matrix.py
+++ b/Ashby_Engine/tests/test_execution_profile_and_adapter_matrix.py
@@ -1,6 +1,6 @@
 from __future__ import annotations
 
-from ashby.core.execution_profiles import get_execution_profile, ExecutionProfile
+from ashby.core.profile import ExecutionProfile, get_execution_profile
 from ashby.modules.meetings.adapters.adapter_matrix import get_meetings_adapter_matrix
 
 
@@ -19,3 +19,12 @@
     assert callable(mat.pdf)
     assert callable(mat.normalize)
     assert callable(mat.align)
+
+
+def test_execution_profiles_shim_exports_canonical_type():
+    # Legacy module should be a thin re-export, not a parallel enum.
+    import ashby.core.execution_profiles as shim_mod
+    import ashby.core.profile as profile_mod
+
+    assert shim_mod.ExecutionProfile is profile_mod.ExecutionProfile
+    assert shim_mod.get_execution_profile is profile_mod.get_execution_profile

```
