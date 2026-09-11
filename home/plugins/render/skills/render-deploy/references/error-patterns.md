# Error patterns (compact)

Consult this reference when error patterns (compact) is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

Use this to quickly map log signatures to likely causes and fixes.

| Log pattern | Likely cause | Quick fix |
| --- | --- | --- |
| `KeyError`, `not defined`, `missing environment` | Missing env var | Add env var in render.yaml or via MCP, then redeploy |
| `EADDRINUSE`, `listen EADDRINUSE` | Port binding conflict | Bind to `0.0.0.0:$PORT` |
| `Cannot find module`, `ModuleNotFoundError` | Missing dependency | Add dependency to manifest and rebuild |
| `ECONNREFUSED`, `connection refused` | DB not reachable | Verify DATABASE_URL and DB status |
| `Health check timeout` | No healthy response | Add/verify health endpoint and port |
| `exit 137`, `out of memory` | OOM | Reduce memory use or upgrade plan |
| `Command failed`, `build failed` | Bad build command | Fix build command or dependencies |
