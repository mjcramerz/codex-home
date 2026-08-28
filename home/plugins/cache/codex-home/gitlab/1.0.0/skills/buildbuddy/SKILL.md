---
name: buildbuddy
description: Design BuildBuddy-backed remote cache and execution workflows with explicit auth, isolation, and fallback behavior. Use when the user asks about BuildBuddy integration, remote execution policy, or Bazel CI acceleration.
metadata:
  version: '1.0'
  short-description: Remote cache and execution policy for Bazel workloads
  tags:
  - buildbuddy
  - bazel
  - cache
  - remote-execution
interface:
  display-name: BuildBuddy
  short-description: Remote cache and execution policy for Bazel workloads
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#2563EB'
  default-prompt: Act as the "BuildBuddy" specialist for "Remote cache and execution policy for Bazel workloads". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing remote cache or remote execution setup for Bazel
- checking BuildBuddy endpoint, auth, or per-runner isolation policy
- planning cache retention, fallback, or secrets handling for shared CI

## Workflow
1) Confirm whether BuildBuddy is used for cache only or for full remote execution.
2) Keep auth tokens, instance names, and endpoint URLs out of tracked config when they are secret-bearing.
3) Document fallback behavior for local execution when the remote service is unavailable.
4) Validate representative Bazel targets with and without remote services before rollout.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Reparse structured config after mutation.
- Run repo-local lint/test/build commands when the touched surface ships them.
- Record residual gaps when external credentials or infrastructure are required for deeper verification.

## Outputs
- Reviewable changes with explicit validation evidence.
- A concise contract summary, the files or jobs touched, and the remaining rollout risks.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/1.0.0/skills/buildbuddy/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/1.0.0/skills/buildbuddy/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/bazel-buildbuddy.md
- $CODEX_HOME/docs/infra/buildbuddy.md
- $CODEX_HOME/index/domains/infra/buildbuddy.md
