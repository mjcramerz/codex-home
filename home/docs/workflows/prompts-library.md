# Prompts library workflow

Use this guide when the task concerns prompts library workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-prompts-library.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

Use `$CODEX_HOME/plans/prompts-library.md` for prompt-library maintenance scope and `$CODEX_HOME/plans/workflows/workflow-prompts-library.md` for workflow execution.

## Source-of-truth rules

- Keep prompt design guidance centralized in `$CODEX_HOME/docs/create-prompts.md`.
- Keep slash command names stable unless rename is explicitly requested.
- Keep `$ARGUMENTS` contracts explicit and consistent with command behavior.

## Maintenance flow

1. Confirm objective, affected prompt assets, and expected behavior.
2. Update `$CODEX_HOME/docs/create-prompts.md` if prompt structure, naming, or guidance changes.
3. Update supporting maintenance assets (template, snippet, skill docs, routing links) when contracts change.
4. Run prompt-focused checks before pack-wide checks.

## Validation sequence

- `rg -n --sort path --color=never '\$ARGUMENTS' $CODEX_HOME/docs $CODEX_HOME/templates $CODEX_HOME/plans`
- Run the narrowest full validation command available for the active Codex worktree.

## Security checkpoints

- Reject prompt changes that encourage bypassing auth, validation, or destructive safeguards.
- Keep input constraints explicit (required args, bounded scope, expected verification).
- Ensure prompt guidance does not leak secrets or request environment dumps.

## Testing checkpoints

- Verify prompt-file guidance remains centralized in `$CODEX_HOME/docs/create-prompts.md`.
- Validate links to entrypoints, plans, and skills after renames or file moves.
- Re-run prompt checks after each follow-up edit to avoid stale references.

## Deployment checkpoints

- Document renamed/retired commands and migration notes for users.
- Keep rollback path available by preserving prior prompt revisions.

## Multi-agent handoff

- Coordinator assigns command/file ownership and success criteria.
- When executing, report changed prompt guidance files, validation evidence, and unresolved gaps.
- Receiver verifies prompt-file guidance still routes through `$CODEX_HOME/docs/create-prompts.md` before next step.

See also:
- `$CODEX_HOME/plans/prompts-library.md`
- `$CODEX_HOME/docs/create-prompts.md`
- `$CODEX_HOME/docs/prompts-maintenance.md`
- `$CODEX_HOME/index/pack/prompts.md`
- Read the `pack-prompts` skill only when its trigger matches this task and the skill is available.
