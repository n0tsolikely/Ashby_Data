# 02_EXECUTION.md

Implemented:
- `src/api/stuartClient.js`: added `registry.get()`.
- `src/hooks/useRegistry.js`: react-query hook with 60s stale time.
- `src/components/stuart/ModeTemplateConfig.jsx`: template merge helpers now prefer `templates_by_mode` payload and fallback to constants.
- `src/components/stuart/RunControls.jsx`: dropdown now uses registry templates with title+id display and loading/error fallback hints.
