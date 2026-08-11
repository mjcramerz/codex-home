# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-release.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/release.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/release.md`
- `$CODEX_HOME/index/core/ci-cd.md`
- `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`

## Scope
- In: release promotion, tag/publish execution, and delivery contract validation.
- Out: non-release feature development.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Route through `$CODEX_HOME/index/core/ci-cd.md`, then execute `$CODEX_HOME/docs/workflows/release.md`.
[ ] Capture release inputs (release source ref, version, release-tag format, approvals, signing context).
[ ] Verify `mcr/staging` gates passed and `mcr/release` tip is the only release source.
[ ] In fork mode, verify `origin/github/mcr/main -> github/mcr/main -> mcr/main` sync and completed patch checks on `mcr/main` before release promotion.
[ ] Validate delivery include mode (`/github/validate.yml` + `/github/push.yml` with shared version/patch/visibility internals) and protected-ref rules.
[ ] Verify release helper scripts exist (for example `scripts/release/get_version.py` and `scripts/release/bump_version.py` in the target repository) and are wired through CI variables.
[ ] Validate release/patch variables against `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env` (`GH_RELEASE_PUSH`, `APPEND_VERSION`, `RELEASE_VERSION`, `VERSION_BUMP_*`, `GH_FORCE_PUSH`, `GH_PUBLIC_REPO`, `APPLY_PATCHES*`, `PATCH_*`, `GH_ORG_RELEASE*`, `GIT_BRANCH_*`).
[ ] When publishing GitLab release assets, validate `/gitlab/validate.yml`, `/gitlab/release.yml`, one stack build include, and `GL_RELEASE_ASSET` companion variables.
[ ] Create and push an annotated release tag on the tip of `mcr/release`.
[ ] Execute release steps in order, capture provenance/signing evidence, and record run URLs plus artifact identifiers.
[ ] Document rollback refs and operator ownership before closing the release.

## Testing and validation
- You must confirm the tag SHA equals `origin/mcr/release` before publish jobs run.
- You must confirm required release jobs complete and record run URLs plus artifact digests.
- Accept only if published artifacts map to the tagged release tip and rollback refs are documented.

## Security checkpoints
- You must verify signing credentials are scoped, valid, and available only to protected release refs.
- You must treat policy bypasses as explicit exceptions with owner, reason, and expiry.

## Testing checkpoints
- You must define pre-tag and post-tag checks with explicit pass criteria.
- You must re-run critical smoke/security checks when release workflows require post-tag validation.

## Deployment checkpoints
- You must keep release order explicit (`mcr/staging` gates -> `mcr/release` tip tag -> publish channels).
- You must record post-release monitoring owner and rollback threshold in release notes.

## Multi-agent handoff
- Coordinator hands off scope, target entrypoint, and stop condition.
- Executor reports touched files, commands, evidence, blockers, and next action.

## Risks and edge cases
- Tagging a non-tip commit can break provenance and rollback guarantees.
- Missing include/variable contracts can pass CI yet fail release publication.
