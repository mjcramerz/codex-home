# Ci cd plan

Use this plan when you following `$CODEX_HOME/docs/workflows/ci-cd.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/ci-cd.md`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- `$CODEX_HOME/docs/workflows/ci-cd.md`
- `$CODEX_HOME/index/core/ci-cd.md`
- `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`

## Scope

- In: CI/CD contract updates and verification for GitHub Actions, GitLab CI, and release handoff.
- Out: non-CI product code changes.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Route through `$CODEX_HOME/index/core/ci-cd.md`, then execute `$CODEX_HOME/docs/workflows/ci-cd.md`.
- [ ] Capture branch/tag policy, protected refs, release tag format, and secret boundaries before editing.
- [ ] Validate branch/tag invariants (`mcr/*` source flow, read-only `github/*` mirrors in fork mode, release tags on the tip of `mcr/release`).
- [ ] In fork mode, validate sync and patch-check order (`origin/github/mcr/main -> github/mcr/main -> mcr/main`, patch checks on `mcr/main`, then promotion to `mcr/staging` and `mcr/release`).
- [ ] Validate GitLab delivery include contract (`GL_CICD_SHARED_PROJ`, `/github/validate.yml`, `/github/push.yml`, plus shared internals `/github/version.yml`, `/patches/patches.yml`, `/github/visibility.yml`).
- [ ] Verify release/patch variable contract against `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env` (`GH_RELEASE_PUSH`, `APPEND_VERSION`, `RELEASE_VERSION`, `VERSION_BUMP_*`, `GH_FORCE_PUSH`, `GH_PUBLIC_REPO`, `APPLY_PATCHES*`, `PATCH_*`, `GH_ORG_RELEASE*`, `GIT_BRANCH_*`).
- [ ] If `GL_RELEASE_ASSET=true`, validate `/gitlab/validate.yml`, `/gitlab/release.yml`, one stack build include, and all `GL_RELEASE_ASSET` companion variables.
- [ ] For GitHub wrappers, verify shared-ref pinning, dispatch-input contracts, and BWS secret wiring.
- [ ] Apply updates in reversible order and record acceptance evidence per platform.

## Testing and validation

- Run deterministic contract checks first (`git fetch origin --prune --prune-tags`, bounded `rg` scans for includes/variables/rules).
- Run platform-specific lint/validation for each edited CI file.
- Accept only if branch/tag gates, include wiring, and variable contracts match workflow guidance.

## Security checkpoints

- Keep stage tokens least-privilege; block release credentials on untrusted refs.
- Record any bypass as a time-boxed exception with owner, reason, and expiry.

## Testing checkpoints

- Define fast-path and deep-path checks with explicit pass criteria before edits.
- Re-run checks after every trigger/rules/include contract change.

## Deployment checkpoints

- Keep promotion order explicit (`mcr/main` -> `mcr/staging` -> `mcr/release` -> release tag).
- Record rollback ref/tag and post-deploy owner before closing the task.

## Multi-agent handoff

- When coordinating, hand off scope, target entrypoint, and stop condition.
- Executor returns touched files, commands, evidence, blockers, and next action.

## Risks and edge cases

- Hidden include overrides or drifted variables can silently break delivery.
- Tag/source mismatch (release tag not at `mcr/release` tip) can publish the wrong artifact.
