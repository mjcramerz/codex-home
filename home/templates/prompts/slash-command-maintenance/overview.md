# Slash command prompt maintenance template
Purpose: tell the Codex coding agent how to use `templates/prompts/slash-command-maintenance/overview.md` as a runtime-pack surface and when to stop browsing.
Use this template when creating or refactoring slash-command prompt files.

## Inputs
- Command name (for example `/my_command`).
- Purpose, boundaries, and acceptance criteria.
- Required arguments and `$ARGUMENTS` contract.
- Linked routing/workflow/plan/skill references.

## Outputs
- `prompt-template.md` adapted for the target command.
- Updated entry in `$CODEX_HOME/docs/create-prompts.md`.
- Validation evidence from prompt and pack checks.

## Steps
1) Create or update the target prompt file in the runtime prompt directory and document it in `$CODEX_HOME/docs/create-prompts.md`.
2) Fill objective, constraints, inputs, and verification sections.
3) Confirm referenced entrypoints and maintenance assets are current.
4) Run prompt checks, then pack checks.

## Next steps
- You must update `$CODEX_HOME/docs/workflows/prompts-library.md` if maintenance flow changed.
- You must update `$CODEX_HOME/snippets/docs/prompt_contract.md` if contract conventions changed.
- You must use skill `pack-prompts` for larger prompt-library edits.
