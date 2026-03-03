# 02_EXECUTION.md

Implemented:
- `tools/proofs/proof_d11_template_lifecycle.py`
  - creates user template via API
  - verifies registry exposure
  - creates deterministic session/run substrate
  - formalizes with fixed template version
  - verifies metadata (id/version/title)
  - exports dev bundle and verifies template internals path entries
- `tests/test_d11_template_lifecycle_proof.py`
  - runs `run_proof(...)` against tmp runtime and asserts success outputs.

Stability fix:
- Switched proof API calls from `TestClient` to `httpx.AsyncClient + ASGITransport` to avoid blocking portal hangs in this environment.
