# Prompts maintenance

Use this guide when the task concerns prompts maintenance. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to creating and maintaining slash-command prompt assets from pack source.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Scope

- Use this guide for maintenance workflow and pack-level coordination only.
- Use `$CODEX_HOME/docs/create-prompts.md` for the actual prompt-file contract and prompt catalog.

## Use this guide when

- adding a new slash command prompt
- refining existing prompt argument contracts (`$ARGUMENTS`)
- removing or renaming prompts safely
- updating prompt-maintenance support assets (routing, workflow, template, snippet, skill)

## Maintenance bundle

- Workflow: `$CODEX_HOME/docs/workflows/prompts-library.md`
- Workflow plan: `$CODEX_HOME/plans/workflows/workflow-prompts-library.md`
- Library plan: `$CODEX_HOME/plans/prompts-library.md`
- Skill: `pack-prompts`
- Template: `$CODEX_HOME/templates/prompts/slash-command-maintenance/`
- Snippet: `$CODEX_HOME/snippets/docs/prompt_contract.md`

## Maintenance flow

1. Confirm whether the change affects prompt content, prompt catalog structure, or both.
2. Update `$CODEX_HOME/docs/create-prompts.md` when prompt names, structure, or catalog membership changes.
3. Update workflow, plan, template, snippet, and skill references when the maintenance surface changes.
4. Run targeted checks before broader repo verification.

## Verification

- Run the narrowest full validation command available for the active Codex worktree.
- Confirm prompt documentation and workflow links still route through `$CODEX_HOME/docs/create-prompts.md`.

## Notes

- Keep command naming deterministic and avoid hidden side effects in prompt instructions.
- Keep links to entrypoints, plans, and skills current when files move.
- Prefer minimal, reviewable prompt diffs with explicit acceptance criteria.
