# Prompts maintenance
Purpose: tell the Codex coding agent how to use `docs/prompts-maintenance.md` as a runtime-pack surface and when to stop browsing.
Guidance for creating and maintaining slash-command prompt assets from pack source.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Scope
- You must use this guide for maintenance workflow and pack-level coordination only.
- You must use `$CODEX_HOME/docs/create-prompts.md` for the actual prompt-file contract and prompt catalog.

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
- You must run the narrowest full validation command available for the active Codex worktree.
- You must confirm prompt documentation and workflow links still route through `$CODEX_HOME/docs/create-prompts.md`.

## Notes
- You must keep command naming deterministic and avoid hidden side effects in prompt instructions.
- You must keep links to entrypoints, plans, and skills current when files move.
- You must prefer minimal, reviewable prompt diffs with explicit acceptance criteria.
