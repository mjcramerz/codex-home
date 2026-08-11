# GitLab Runner
Purpose: guide GitLab Runner host configuration, service-account policy, and executor storage layout for the Codex coding agent.

## Use this guide when
- provisioning or reviewing runner service accounts, tags, or executor policy
- validating managed env-file layout for build, release, and Aptly runner roles
- checking persistent state, cache, Podman, or helper-doc staging for runner hosts

## Baseline
- Keep runner roles split into shared and per-role env fragments so Aptly, build, and Bazel workloads stay independently reviewable.
- Prefer nologin service accounts for non-interactive roles; document any helper path that intentionally runs as a user shell.
- Keep runner state, cache, build, and Podman roots explicit and separate so retention, ownership, and cleanup stay deterministic.
- Treat runner tags, registry credentials, and remote cache tokens as protected CI/runtime inputs, never tracked defaults.

## Validation ladder
1. Verify service-account ownership, modes, and env-file staging.
2. Confirm runner tags and executor type match the intended workload.
3. Run the narrowest repo-local smoke or functional checks for the touched helper or env contract.
4. Recheck docs/readme surfaces when operator-facing behavior changes.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/gitlab-runner.md`
- `$CODEX_HOME/docs/workflows/gitlab-ci.md`
- `$CODEX_HOME/index/domains/system/gitlab-runner.md`
- `$CODEX_HOME/index/core/ci-cd.md`
