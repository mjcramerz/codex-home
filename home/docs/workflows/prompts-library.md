# Prompts library workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-prompts-library.md` before executing this workflow.
Purpose: maintain the prompt-design workflow and supporting prompt-maintenance assets for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan

Use `$CODEX_HOME/plans/prompts-library.md` for prompt-library maintenance scope and `$CODEX_HOME/plans/workflows/workflow-prompts-library.md` for workflow execution.

## Source-of-truth rules
- You must keep prompt design guidance centralized in `$CODEX_HOME/docs/create-prompts.md`.
- You must keep slash command names stable unless rename is explicitly requested.
- You must keep `$ARGUMENTS` contracts explicit and consistent with command behavior.

## Maintenance flow
1) Confirm objective, affected prompt assets, and expected behavior.
2) Update `$CODEX_HOME/docs/create-prompts.md` if prompt structure, naming, or guidance changes.
3) Update supporting maintenance assets (template, snippet, skill docs, routing links) when contracts change.
4) Run prompt-focused checks before pack-wide checks.

## Validation sequence
- `rg -n --sort path --color=never '\$ARGUMENTS' $CODEX_HOME/docs $CODEX_HOME/templates $CODEX_HOME/plans`
- You must run the narrowest full validation command available for the active Codex worktree.

## Security checkpoints
- Reject prompt changes that encourage bypassing auth, validation, or destructive safeguards.
- You must keep input constraints explicit (required args, bounded scope, expected verification).
- Ensure prompt guidance does not leak secrets or request environment dumps.

## Testing checkpoints
- You must verify prompt-file guidance remains centralized in `$CODEX_HOME/docs/create-prompts.md`.
- You must validate links to entrypoints, plans, and skills after renames or file moves.
- You must re-run prompt checks after each follow-up edit to avoid stale references.

## Deployment checkpoints
- You must document renamed/retired commands and migration notes for users.
- You must keep rollback path available by preserving prior prompt revisions.

## Multi-agent handoff
- Coordinator assigns command/file ownership and success criteria.
- Executor reports changed prompt guidance files, validation evidence, and unresolved gaps.
- Receiver verifies prompt-file guidance still routes through `$CODEX_HOME/docs/create-prompts.md` before next step.

See also:
- `$CODEX_HOME/plans/prompts-library.md`
- `$CODEX_HOME/docs/create-prompts.md`
- `$CODEX_HOME/docs/prompts-maintenance.md`
- `$CODEX_HOME/index/pack/prompts.md`
- You must use skill `pack-prompts`.
