# Using templates
Purpose: tell the Codex coding agent how to use `docs/templates/using-templates.md` as a runtime-pack surface and when to stop browsing.
Templates are scaffolds you can copy into a repository.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/templates/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- Template source path and destination repository path.
- Exact versions/digests for runtimes, images, and actions.
- Repo-specific values for placeholders, secrets, and environment paths.
- Branch/tag and release policy used by your CI system.

## Outputs
- Template files copied with deterministic paths and preserved modes (`cp -a`).
- Placeholder values replaced (`CHANGE_ME`, sample org/version names).
- A runnable baseline that follows the template's own `overview.md`.

## Deterministic flow
1) Copy the template.
2) Open the copied template `overview.md` and apply only required edits.
3) Replace placeholders and pin versions/digests before first commit.
4) Ensure lockfiles are present and committed (`Cargo.lock`, `package-lock.json`, and similar).
5) Run the narrowest relevant checks (lint/test/build/dry-run) locally and in CI.

## CI and delivery guardrails
- GitHub Actions baseline: `$CODEX_HOME/templates/ci/github-actions/`.
- GitLab CI baseline: `$CODEX_HOME/templates/ci/gitlab-ci/`.
- Perl runtime/hook baseline: `$CODEX_HOME/templates/perl/codex-hook-module/`.
- For Cloudflare R2 publication, route through
  `$CODEX_HOME/docs/workflows/cloudflare-r2.md` before editing storage or
  publication scaffolds.
- Keep shared include ownership explicit; do not duplicate internal include
  graphs unless intentionally forking behavior.
- You must keep protected release refs, patch ordering, and publish mutation order explicit in repo-local docs when a template adopts those flows.

## Next steps
1) Add repo hygiene files from `$CODEX_HOME/templates/common/` (`SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`).
2) Add domain templates you need (`infra/`, `containers/`, `observability/`, `systemd/`, `system/`, `desktop/`).
3) Keep only the sections/files your repo actually uses; remove scaffolding you do not adopt.
