# 03_VERIFY.md

Live receipts captured with provided GEMINI_API_KEY.

- `/health` -> HTTP 200, provider `gemini`, model `gemini-2.5-flash`
- `/v1/formalize` -> HTTP 200
- response includes:
  - `version=1`
  - `request_id`
  - `output_json`
  - `usage`

Response SHA256:
- `6e03ed560b196e36066ae3e00e82084fadbc52791cd2f275c82f2e6638a836bf` (`response_live.json`)
