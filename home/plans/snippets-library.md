# Plan
Purpose: tell the Codex coding agent how to use `plans/snippets-library.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when adding or updating snippets.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Requirements
- Snippets are organized by domain or language.
- overview catalog is updated.

## Scope
- In: `$CODEX_HOME/snippets/` and related index entries.
- Out: unrelated pack changes.

## Files and entry points
- `$CODEX_HOME/snippets/OVERVIEW.md`
- `$CODEX_HOME/index/pack/snippets.md`
- `$CODEX_HOME/docs/OVERVIEW.md`

## Action items
[ ] Add or update snippet files with clear names and comments.
[ ] Update `$CODEX_HOME/snippets/OVERVIEW.md` with new entries.

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
- Duplicate snippets or conflicting patterns.
- Missing discoverability links.

## Examples

- Example objective: "Add a new hardened snippet and document where it should be used."
- Example validation: "run the smallest syntax and contract checks for the touched snippet surface"

## Open questions
- None.
