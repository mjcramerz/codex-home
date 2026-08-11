# BuildBuddy
Purpose: guide BuildBuddy remote cache and remote execution integration for the Codex coding agent.

## Use this guide when
- configuring BuildBuddy-backed remote cache or remote execution for Bazel
- reviewing auth, instance name, or endpoint boundaries for shared runner infrastructure
- validating cache isolation, fallback behavior, or artifact retention expectations

## Baseline
- Confirm whether the deployment uses cache-only or full remote execution before changing flags.
- Keep remote cache and execution endpoints explicit; avoid inheriting them through opaque shell wrappers.
- Isolate credentials per runner or environment, and prefer read-only cache access where execution is not required.
- Document fallback behavior for local execution when the remote service is unavailable.

## Validation ladder
1. Verify endpoint URLs, auth source, and instance naming.
2. Check the exact Bazel flags or env exports used by CI.
3. Run a representative target with and without the remote service if the risk warrants it.
4. Recheck operator docs whenever auth or fallback behavior changes.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/bazel-buildbuddy.md`
- `$CODEX_HOME/docs/infra/bazel.md`
- `$CODEX_HOME/index/domains/infra/buildbuddy.md`
