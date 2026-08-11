# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-gitlab-ci.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/gitlab-ci.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/gitlab-ci.md`
- `$CODEX_HOME/index/core/ci-cd.md`
- `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`

## Scope
- In: `.gitlab-ci.yml` contract updates for protected refs, shared includes, and delivery variables.
- Out: GitHub wrapper logic changes that do not affect GitLab orchestration.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Route through `$CODEX_HOME/index/core/ci-cd.md`, then execute `$CODEX_HOME/docs/workflows/gitlab-ci.md`.
[ ] Capture protected-ref rules, include source, release-tag policy, and secret scope before editing.
[ ] Validate `.gitlab-ci.yml` rules for `mcr/staging`, `mcr/release`, protected release tags, and explicit blocks for `main`/`mcr/main` delivery paths.
[ ] In fork mode, validate sync + patch-check order (`origin/github/mcr/main -> github/mcr/main -> mcr/main`, patch checks on `mcr/main`, then `mcr/staging` and `mcr/release` promotions).
[ ] When GitHub publishing is enabled, validate include wiring (`GL_CICD_SHARED_PROJ`, `/github/validate.yml`, `/github/push.yml`) and shared internals (`/github/version.yml`, `/patches/patches.yml`, `/github/visibility.yml`).
[ ] Validate release/version/patch variables against `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env` (`GH_RELEASE_PUSH`, `APPEND_VERSION`, `RELEASE_VERSION`, `VERSION_BUMP_*`, `GH_FORCE_PUSH`, `GH_PUBLIC_REPO`, `APPLY_PATCHES*`, `PATCH_*`, `GH_ORG_RELEASE*`, `GIT_BRANCH_*`).
[ ] When GitLab package release is enabled, validate `/gitlab/validate.yml`, `/gitlab/release.yml`, one stack build include, and `GL_RELEASE_ASSET` companion variables.
[ ] Validate patch defaults (`patches/release`, `patches/release/series`) and mutation order (`checkout -> true sync -> version bump -> patch apply -> push`).
[ ] Validate required secret contracts (`GH_ORG_RELEASE*`, `BWS_*`) stay protected and scoped to trusted refs.
[ ] Apply updates in reversible order and capture acceptance evidence.

## Testing and validation
- You must run GitLab CI lint and targeted pipeline checks for changed include/rules paths.
- You must run deterministic contract scans (`rg` for includes, vars, refs) before broad pipeline runs.
- Accept only if protected-ref rules, include wiring, and variable contracts match the workflow guide.

## Security checkpoints
- Restrict release jobs and protected variables to trusted refs only.
- You must treat runner privilege or secret-scope exceptions as time-boxed approvals with owner and expiry.

## Testing checkpoints
- You must define fast-path and deep-path checks with explicit pass criteria before edits.
- You must re-run checks after include, rules, or variable contract changes.

## Deployment checkpoints
- You must keep promotion order explicit (`mcr/staging` validation -> `mcr/release` -> protected release tag).
- You must record rollback artifact refs and release operator ownership in handoff notes.

## Multi-agent handoff
- Coordinator hands off scope, target entrypoint, and stop condition.
- Executor reports touched files, commands, evidence, blockers, and next action.

## Risks and edge cases
- Shared include drift can bypass required validation/push jobs.
- Variable drift against `gitlab_delivery_vars.env` can break release promotion.
