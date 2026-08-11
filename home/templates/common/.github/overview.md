# Common .github templates (overview)
Purpose: tell the Codex coding agent how to use `templates/common/.github/overview.md` as a runtime-pack surface and when to stop browsing.
Repository hygiene defaults for dependency updates and pull request quality.

## Inputs
- Dependency update cadence and ecosystem coverage.
- Reviewer/label policy for automated update PRs.
- Pull request checklist sections and approval expectations.

## Outputs
- `dependabot.yml`
- `pull_request_template.md`

## Usage
1) Copy files into `.github/` at the active runtime context.
2) Customize update schedules, package ecosystems, and labels in `dependabot.yml`.
3) Tailor PR checklist/content in `pull_request_template.md` for team workflow.
4) Validate that branch protections align with the checklist and update policy.

## Next steps
- Pair with baseline repo files in `$CODEX_HOME/templates/common/` (`CODEOWNERS`, `SECURITY.md`, `CONTRIBUTING.md`).
- You must keep contribution/security guidance aligned with workflow docs in `$CODEX_HOME/docs/workflows/repo-ops.md`.

Related:
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/docs/templates/using-templates.md`
- `$CODEX_HOME/docs/workflows/repo-ops.md`
