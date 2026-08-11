# Plan
Purpose: tell the Codex coding agent how to use `plans/rules-library.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when updating execpolicy rules or guidance.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Requirements
- Rules are documented with clear intent and ordering.
- Execpolicy docs and indexes are updated.

## Scope
- In: `$CODEX_HOME/rules/` and related runtime documentation and index entries.
- Out: unrelated pack changes.

## Files and entry points
- `$CODEX_HOME/rules/OVERVIEW.md`
- `$CODEX_HOME/index/pack/rules.md`
- `$CODEX_HOME/index/core/execpolicy.md`
- `$CODEX_HOME/docs/workflows/execpolicy.md`

## Action items
[ ] Add or update rule files with explicit intent and scope.
[ ] Update `$CODEX_HOME/rules/OVERVIEW.md` to document ordering and constraints.
[ ] Update execpolicy docs and index references.

## Testing and validation

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- You must record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints
- You must define fast-path and deep validation commands before making changes.
- You must capture expected outcomes and acceptance criteria for each validation step.
- You must re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints
- You must document rollout order, blast-radius controls, and rollback conditions.
- You must confirm migration/backfill or feature-flag sequencing when applicable.
- You must record post-deploy verification owners and evidence.

## Multi-agent handoff
- Coordinator hands off scope, constraints, and stop condition with the target entrypoint.
- Executor reports touched files, commands run, evidence, blockers, and next action.
- Receiving agent acknowledges handoff completeness before continuing execution.

## Risks and edge cases
- Rule ordering conflicts.
- Missing references in docs or index.

## Examples

- Example objective: "Update execpolicy rule guidance after adding a new command family."
- Example validation: "run the smallest syntax and contract checks for the touched rules surface"

## Open questions
- None.
