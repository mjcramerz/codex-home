# Common .github templates (overview)

Use this template when you need common .github templates (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Repository hygiene defaults for dependency updates and pull request quality.

## Inputs

- Dependency update cadence and ecosystem coverage.
- Reviewer/label policy for automated update PRs.
- Pull request checklist sections and approval expectations.

## Outputs

- `dependabot.yml`
- `pull_request_template.md`

## Usage

1. Copy files into `.github/` at the active runtime context.
2. Customize update schedules, package ecosystems, and labels in `dependabot.yml`.
3. Tailor PR checklist/content in `pull_request_template.md` for team workflow.
4. Validate that branch protections align with the checklist and update policy.

## Next steps

- Pair with baseline repo files in `$CODEX_HOME/templates/common/` (`CODEOWNERS`, `SECURITY.md`, `CONTRIBUTING.md`).
- Keep contribution/security guidance aligned with workflow docs in `$CODEX_HOME/docs/workflows/repo-ops.md`.

Related:
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/docs/templates/using-templates.md`
- `$CODEX_HOME/docs/workflows/repo-ops.md`
