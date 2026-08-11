---
name: bazel
description: Plan Bazel build and test workflows with hermetic toolchains, cache discipline, and CI-safe remote execution boundaries. Use when the user asks about Bazel commands, CI wiring, or repository/runner layout for Bazel workloads.
metadata:
  version: '1.0'
  short-description: Hermetic Bazel builds in shared CI and runner environments
  tags:
  - bazel
  - build
  - ci
  - hermetic
interface:
  display-name: Bazel
  short-description: Hermetic Bazel builds in shared CI and runner environments
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#2563EB'
  default-prompt: Act as the "Bazel" specialist for "Hermetic Bazel builds in shared CI and runner environments". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing Bazel workspace, build, or test job structure
- checking remote cache/execution variables or output-base placement
- aligning Bazel jobs with runner tags, artifact retention, or package promotion steps

## Workflow
1) Confirm Bazel version, workspace root, and whether remote cache or execution is enabled.
2) Keep repository rules, toolchains, and cache endpoints pinned and reviewable.
3) Separate fast local verification from heavier remote-execution or release build jobs.
4) Validate the exact target set and cache policy touched by the change before widening scope.

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
- `$CODEX_HOME/plugins/cache/codex-local/gitlab/local/skills/bazel/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/gitlab/local/skills/bazel/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/bazel-buildbuddy.md
- $CODEX_HOME/docs/infra/bazel.md
- $CODEX_HOME/index/domains/infra/bazel.md
