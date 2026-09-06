---
name: gitlab-cicd
description: Author and review GitLab CI/CD pipelines that stay thin over shared include contracts, protected refs, runner tags, and release-safe variable policies. Use when the user asks about .gitlab-ci.yml structure, include boundaries, or GitLab delivery hardening.
metadata:
  version: '1.0'
  short-description: Thin consumer pipelines over shared include contracts
  tags:
  - gitlab
  - ci
  - cicd
  - delivery
interface:
  display-name: GitLab CI/CD
  short-description: Thin consumer pipelines over shared include contracts
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#FC6D26'
  default-prompt: Act as the "GitLab CI/CD" specialist for "Thin consumer pipelines over shared include contracts". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- creating or hardening `.gitlab-ci.yml` files
- validating `GL_CICD_SHARED_PROJ` include usage and protected-ref rules
- reviewing release-tag, mirror-sync, or package publishing job behavior

## Workflow
1) Define stages, workflow rules, and protected ref behavior before changing jobs.
2) Keep consumer pipelines thin; prefer shared includes for policy, publish, and delivery internals.
3) Pin build images, runner tags, and secrets scope explicitly in variables or protected CI settings.
4) Validate include wiring, mutation order, and guarded release behavior with the narrowest repo-local checks.

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
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/1.0.0/skills/gitlab-cicd/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/1.0.0/skills/gitlab-cicd/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/gitlab-ci.md
- $CODEX_HOME/docs/workflows/ci-cd.md
- $CODEX_HOME/index/core/ci-cd.md
