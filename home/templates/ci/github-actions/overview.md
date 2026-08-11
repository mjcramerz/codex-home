# GitHub Actions templates (overview)
Purpose: tell the Codex coding agent how to use `templates/ci/github-actions/overview.md` as a runtime-pack surface and when to stop browsing.
Pinned starter workflows for common language stacks and baseline security checks.

## Inputs
- Repository language/runtime targets (Node, Python, Rust).
- Branch and trigger policy for pull requests, pushes, and release automation.
- Required secrets, tokens, and least-privilege permissions.
- Optional wrapper dispatch contract (`event-context`, `event-name`, `expected-event-action`, `target-org`, `shared-repo`, `shared-ref`) when integrating with `gh-actions-shared`.

## Outputs
- `node.yml`
- `python.yml`
- `rust.yml`
- `security.yml`
- `release-build.yml`
- `release-publish.yml`

## Deterministic usage
1) Copy needed files into `.github/workflows/` in your repository.
2) Pin action refs to immutable commits and set explicit runtime versions to match your support policy.
3) Set minimal workflow permissions and wire required secrets.
4) Keep branch filters aligned with protected refs (`mcr/main`, `mcr/staging`, `mcr/release`) unless repo policy differs.
5) Run workflows in a pull request before requiring them on protected branches.
6) For release workflows, enforce your protected release-tag contract and require tags to point at the tip of `mcr/release`.
7) Keep release publishing on `release-from-workflow-run.yml` (it runs shared OSV security gates before publishing) and add `security.yml` only when non-release branch/PR scans are required.
8) If a Cloudflare worker dispatches workflows, verify `GH_WORKFLOW_REF` and branch-policy env settings stay aligned with `gh-actions-shared`.

## Next steps
1) Align triggers/rules with `$CODEX_HOME/docs/workflows/github-actions.md`.
2) Apply least-privilege defaults from `$CODEX_HOME/snippets/ci/github_actions_min_permissions.yml`.
3) Keep wrapper/release variable contracts aligned with `$CODEX_HOME/snippets/ci/github_release_vars.env`.
4) Run one successful PR/tag validation before making checks required.

Related:
- `$CODEX_HOME/docs/workflows/github-actions.md`
- `$CODEX_HOME/docs/workflows/ci-cd.md`
- `$CODEX_HOME/snippets/ci/github_actions_min_permissions.yml`
- `$CODEX_HOME/snippets/ci/github_release_vars.env`
