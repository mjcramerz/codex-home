# Plan
Purpose: tell the Codex coding agent how to use `plans/templates-library.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when adding or updating templates.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Requirements
- Template overviews explain usage and constraints.

## Scope
- In: `$CODEX_HOME/templates/` and related runtime documentation and index entries.
- Out: unrelated pack changes.

## Files and entry points
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/index/pack/templates.md`
- `$CODEX_HOME/docs/templates/overview.md`

## Action items
[ ] Add or update template directories and overview files.
[ ] Update `$CODEX_HOME/templates/OVERVIEW.md` with new entries.

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
- Templates missing usage notes.

## Examples

- Example objective: "Update a template family and keep its overview plus linked docs aligned."
- Example validation: "run the smallest syntax and render checks for the touched template family"

## Open questions
- None.
