# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-memory-runtime.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when removing or replacing legacy references to `$CODEX_HOME/docs/workflows/memory-runtime.md`.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Inputs
- `$CODEX_HOME/docs/workflows/memory-runtime.md`
- `$CODEX_HOME/docs/workflows/repo-ops.md`

## Scope
- In: retiring stale `codex-db-fetch` / `$CODEX_ROOT/mem/*` guidance.
- Out: recreating the removed memory-transfer workflow.

## Action items
[ ] Confirm the affected files only contain legacy memory-runtime references.
[ ] Remove or rewrite each `codex-db-fetch` and `$CODEX_ROOT/mem/*` reference.
[ ] Route replacement guidance to `repo-ops.md` as appropriate.
[ ] Run targeted searches to confirm the retired commands/paths are gone from touched docs.
[ ] Run the narrowest relevant validation before handoff.

## Testing and validation
- You must run `rg -n --sort path --color=never 'codex-db-fetch|\$CODEX_ROOT/mem' $CODEX_HOME`.
- You must run the narrowest relevant validation after the cleanup lands.

## Security checkpoints
- You must treat any request to restore the removed flow as a separate behavior change requiring approval.

## Testing checkpoints
- You must capture search output before and after edits.
- You must record the replacement entrypoint used for each rewritten doc.

## Deployment checkpoints
- Land the cleanup before telling operators to use the affected guidance.

## Multi-agent handoff
- Explorer inventories stale references only.
- One owner rewrites the guidance and reports verification evidence.

## Risks and edge cases
- Hidden references in generated/runtime mirrors may linger if the sweep is incomplete.

## Open questions
- None.
