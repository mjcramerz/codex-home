---
name: ci-github-actions
description: Design or update GitHub Actions pipelines with pinned tooling, least-privilege
  permissions, caching strategy, and reproducible CI gates. Use when the user asks to create,
  optimize, or harden GitHub Actions YAML configuration.
metadata:
  version: '1.3'
  short-description: Harden GitHub Actions with deterministic, least-privilege defaults
  tags:
  - ci
  - github-actions
  - security
  - testing
interface:
  display-name: CI-GitHub Actions
  short-description: Harden GitHub Actions with deterministic, least-privilege defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3251CC'
  default-prompt: Act as the "CI-GitHub Actions" specialist for "Harden GitHub Actions with
    deterministic, least-privilege defaults". Deliver focused, deterministic results with
    minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

## Use this skill when
- creating or updating `.github/workflows/*`
- hardening wrapper dispatch workflows and shared workflow callsites
- enforcing permission minimization, release-tag guards, and deterministic CI behavior

## Inputs
- target workflows/jobs to change
- branch/tag policy (`mcr/main`, `mcr/staging`, `mcr/release`, protected release tags)
- secrets model (GitHub secrets, BWS, environment-scoped secrets)
- wrapper contract requirements (`event-context`, `event-name`, `expected-event-action`, `target-org`, `shared-repo`, `shared-ref`)

## Scope and boundaries
- Keep wrappers thin; validation/orchestration logic should stay in shared workflows.
- In fork mode, treat `github/mcr/main` and `github/mcr/staging` as read-only mirrors.
- Keep release workflows constrained to protected release tags pointing to the tip of `mcr/release`.
- In fork mode, verify sync order `origin/github/mcr/main -> github/mcr/main -> mcr/main` before patch checks.
- In fork mode, run release patch checks on `mcr/main` only before promoting to `mcr/staging`/`mcr/release`.

## Workflow
1) Confirm trust boundary and trigger model (`pull_request`, protected `push`, `workflow_dispatch`, tags).
2) Apply deterministic edits (pinned actions/runners, lockfile installs, explicit timeouts, controlled concurrency).
3) Keep default `permissions` read-only; scope write grants per job with explicit justification.
4) Validate wrapper inputs and shared-ref pinning/allowlist behavior.
5) Validate release constraints (protected release tags, release-tip checks, artifact path/provenance assumptions, and repo-specific tag contract), and prefer shared `release-from-workflow-run.yml` security gates over duplicated per-repo release scan jobs.
6) Summarize risk, rollback path, and any manual gates.

## Delivery contracts
- Wrapper `shared-repo` and `shared-ref` allowlist alignment.
- Release guardrails for protected release tags and tip checks against `mcr/release`.
- Shared release workflow contract: `release-from-workflow-run.yml` runs `security-gates.yml` before publishing; keep caller refs pinned to immutable commit SHAs.
- Repository variable contract from `$CODEX_HOME/snippets/ci/github_release_vars.env`.

## Agent orchestration
- Delegate read-only discovery (workflow inventory, failed runs, permission deltas).
- Reconcile findings centrally before changing shared workflow callsites.

## Validation and testing
- Run `actionlint` (or repo equivalent) for syntax and policy failures.
- Exercise only affected trigger paths/matrix slices and avoid full workflow churn.
- Confirm permission deltas, secrets exposure boundaries, and cache-key determinism.
- Recheck release-tag behavior when tag or publish jobs change.

## Outputs
- Minimal, reviewable workflow diffs.
- Explicit trigger/permission rationale.
- Verification evidence and follow-up checks.

## References
- `$CODEX_HOME/docs/workflows/github-actions.md`
- `$CODEX_HOME/docs/workflows/ci-cd.md`
- `$CODEX_HOME/templates/ci/github-actions/`
- `$CODEX_HOME/snippets/ci/github_actions_min_permissions.yml`
- `$CODEX_HOME/snippets/ci/github_release_vars.env`
