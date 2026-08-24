---
name: gitlab-runner
description: Operate GitLab Runner host configurations with explicit service-account, runner-tag, Podman, Aptly, and cache-root contracts. Use when the user asks about runner provisioning, executor policy, or managed environment file layout.
metadata:
  version: '1.0'
  short-description: Service-account, runner-tag, and execution-root contracts
  tags:
  - gitlab
  - runner
  - podman
  - service
interface:
  display-name: GitLab Runner
  short-description: Service-account, runner-tag, and execution-root contracts
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#FC6D26'
  default-prompt: Act as the "GitLab Runner" specialist for "Service-account, runner-tag, and execution-root contracts". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing runner service-account, executor, or environment-file policy
- checking runner tags, persistent cache roots, or rootless container layout
- verifying how build, release, Aptly, or Bazel workloads are split across runner roles

## Workflow
1) Confirm executor type, service account shell policy, and runner-tag contract first.
2) Keep per-role env fragments separate from shared runner storage and Podman policy.
3) Stage generated helper scripts and docs as deterministic assets instead of inline one-offs.
4) Validate with the narrowest runner smoke tests and ownership/mode checks before rollout.

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
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/local/skills/gitlab-runner/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/local/skills/gitlab-runner/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/gitlab-runner.md
- $CODEX_HOME/docs/system/gitlab-runner.md
- $CODEX_HOME/index/domains/system/gitlab-runner.md
