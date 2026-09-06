---
name: ci-gitlab-cicd
description: Build and troubleshoot GitLab CI/CD pipelines with deterministic jobs, pinned images, shared include contracts, and protected delivery gates. Use when the user asks to create or fix `.gitlab-ci.yml` pipelines, shared GitLab delivery includes, or release-safe variable policy.
metadata:
  version: '1.2'
  short-description: Build deterministic GitLab pipelines with shared include and delivery discipline
  tags:
  - gitlab
  - ci
  - cd
  - delivery
  - security
interface:
  display-name: CI-GitLab CI/CD
  short-description: Build deterministic GitLab pipelines with shared include and delivery discipline
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#4432CC'
  default-prompt: Act as the "CI-GitLab CI/CD" specialist for "Build deterministic GitLab pipelines with shared include and delivery discipline". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- creating or hardening `.gitlab-ci.yml` pipelines
- validating `GL_CICD_SHARED_PROJ` include boundaries and protected-ref rules
- wiring GitLab to GitHub delivery, optional GitLab package publishing, or repo-local CI command variables
- fixing rules, runner, image, or variable drift in shared delivery pipelines

## Inputs
- target `.gitlab-ci.yml` and included templates
- protected ref policy (`mcr/staging`, `mcr/release`, protected release tags)
- delivery intent (GitHub sync only, sync plus GitLab package publishing, or domain-specific deploy includes)
- shared include defaults, runner-tag policy, and repo-local variable overrides

## Scope and boundaries
- Treat `GL_CICD_SHARED_PROJ` as a CI variable that must already exist before top-level includes resolve.
- Keep consumer pipelines thin and explicit about stages, runner tags, image pins, and overrides.
- Keep shared internals centralized unless the user explicitly requests a contract fork.
- Preserve deterministic mutation order for delivery jobs and keep mirror branches read-only in fork workflows.
- Do not copy host-specific repository paths into generated guidance; refer to include names, contracts, and runtime paths instead.

## Workflow
1) Define stage graph, protected-ref rules, and the intended include graph first.
2) Apply deterministic include and variable contracts; avoid per-repo drift.
3) Keep runner tags, images, and command variables explicit and reviewable.
4) Keep patch ordering authoritative where release overlays are in play.
5) If package publishing is enabled, validate the publish include contract and companion variables together.
6) If Bazel, BuildBuddy, or image-build jobs are involved, keep those variables and caches scoped to the jobs that need them.
7) Validate the minimal impacted jobs and report residual risk.

## Agent orchestration
- Delegate read-only graph inspection and include/variable audits.
- Reconcile before editing shared blocks or release jobs.

## Validation and testing
- Lint `.gitlab-ci.yml` and verify include resolution before runtime checks.
- Run deterministic contract scans (`rg` or similar) for include paths, variables, and protected-ref rules.
- Run narrow stage smoke tests only for the jobs affected by the change.
- Confirm logs/artifacts do not leak secret values or token material.

## Outputs
- Reviewable `.gitlab-ci.yml` diffs with clear delivery rationale.
- Contract checklist (includes, vars, mutation order, protected refs, runner or image policy).
- Verification evidence.

## References
- `$CODEX_HOME/docs/workflows/gitlab-ci.md`
- `$CODEX_HOME/docs/workflows/gitlab-runner.md`
- `$CODEX_HOME/docs/workflows/release.md`
- `$CODEX_HOME/templates/ci/gitlab-ci/`
- `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`
