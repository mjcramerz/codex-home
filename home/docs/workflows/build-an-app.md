# Workflow: build an app (end-to-end)

You must start with `$CODEX_HOME/plans/workflows/workflow-build-an-app.md` before executing this workflow.
Purpose: a reliable, repeatable path from idea to a secure, testable MVP for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## 1) Define scope
- MVP vs production target
- Required endpoints/features and non-goals
- Data persistence and auth strategy
- Deployment target (local, container, cloud)

## 2) Select a template
- Python API: `$CODEX_HOME/templates/python/fastapi-app`
- Rust API: `$CODEX_HOME/templates/rust/axum-api`
- Web app: `$CODEX_HOME/templates/web/react-vite-app`
- CLI apps: `$CODEX_HOME/templates/python/cli-app`, `$CODEX_HOME/templates/rust/cli-app`
- Containers/VMs: `$CODEX_HOME/templates/containers/`, `$CODEX_HOME/templates/virtualization/`


## 3) Wire baseline (before features)
- Config validation at startup
- Structured logging + request IDs (APIs)
- Error handling without leaking internals
- Health endpoint and basic tests
- Security headers and request limits (APIs)

## 4) Implement a vertical slice
- One feature end-to-end with tests.
- You must keep diffs small and reviewable.

## 5) Hardening pass
- Input validation + explicit size limits.
- Timeouts and bounded retries on all I/O.
- You must add rate limiting/quotas if public-facing.
- Dependency audits and lockfiles.

## 6) CI/CD
- You must add workflows from `$CODEX_HOME/templates/ci/github-actions/` or `$CODEX_HOME/templates/ci/gitlab-ci/`.
- Lint, test, and audit gates with minimal permissions.

## Branching & release flow
- Implement directly on `mcr/main` only after checks and boundaries are clear.
- Promote tested changes in order: `mcr/main -> mcr/staging -> mcr/release`.
- In the restricted mirror workflow (`github/mcr/main` or `gitlab/mcr/main` exists), treat `github/*` and `gitlab/*` as read-only and never implement directly on mirror branches.
- In the restricted mirror workflow, sync mirror main into `mcr/main` before release patch checks.
- In the restricted mirror workflow, run release patch checks on `mcr/main` only and keep `mcr/main` edits within the repository-root allowlist unless a deeper repo contract expands scope.
- For GitLab-delivered GitHub releases, tag from the tip of `mcr/release` using your protected release tag contract.
- You must keep delivery mutation order deterministic for release syncs: `checkout -> true sync -> version bump -> patch apply -> push` (with patches sourced from `patches/release/series`).

## Deterministic build checklist
- Pin toolchains and base images; avoid `:latest`.
- Commit lockfiles and use deterministic installs (`cargo --locked`, `npm ci`, `pnpm install --frozen-lockfile`).
- You must keep version changes script-driven through the target repository's release helper scripts (for example `scripts/release/get_version.py` and `scripts/release/bump_version.py`).

## 7) Docs + runbook
- You must update README with setup/run/test commands.
- You must document config and operational notes.

## Security checkpoints
- Lock auth model, trust boundaries, and secret storage approach before shipping the first endpoint.
- Enforce request/body/file-size limits and timeout defaults in the initial scaffold.
- Audit new dependencies before merge and document any temporary vulnerability waiver.

## Testing checkpoints
- You must require one happy-path and one abuse-path test for each externally reachable feature slice.
- You must keep startup, health, and config-validation checks in the always-on smoke suite.
- Gate merges on template-aligned lint/unit/integration commands captured in README or CI.

## Deployment checkpoints
- You must define the environment contract (required vars, secrets source, migrations) before first deploy.
- Promote local -> staging -> production with health checks and explicit rollback criteria.
- Publish a runbook with release command, rollback command, and on-call owner.

## Multi-agent handoff
- Feature owner hands API/schema contract and config deltas to test and deploy owners.
- Test owner hands failing repro, added tests, and expected outputs back to implementer.
- Release owner confirms artifact version/digest and rollout status before final sign-off.
See also:
- `overview.md`
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/index/pack/workflows.md`
