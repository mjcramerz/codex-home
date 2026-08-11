# Bazel
Purpose: guide Bazel workspace, cache, and CI execution policy for the Codex coding agent.

## Use this guide when
- reviewing Bazel workspace, test, or release jobs
- validating remote cache or remote execution behavior in shared runners
- checking toolchain pinning and hermetic build guarantees

## Baseline
- Keep Bazel version selection explicit and reviewable (for example via Bazelisk or pinned installer packages).
- Separate local developer defaults from CI executor defaults so remote cache or execution settings do not leak unexpectedly.
- Treat `.bazelrc`, repository rules, and toolchains as contract surfaces whenever CI behavior changes.
- Keep cache credentials and remote endpoint tokens out of tracked files.

## Validation ladder
1. Verify the effective Bazel version and workspace root.
2. Check `.bazelrc`, cache/execution flags, and target selection.
3. Run the smallest target set that proves the changed contract.
4. Recheck CI wiring when Bazel behavior is consumed through GitLab jobs.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/bazel-buildbuddy.md`
- `$CODEX_HOME/docs/infra/buildbuddy.md`
- `$CODEX_HOME/index/domains/infra/bazel.md`
- `$CODEX_HOME/index/core/ci-cd.md`
