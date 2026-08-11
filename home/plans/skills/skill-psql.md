# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-psql.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `psql` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill psql.
- Any referenced scripts, assets, or references in the skill

## Scope
- In: tasks covered by the `psql` skill and its resources.
- Out: tasks outside the skill’s domain.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Use skill psql and linked resources.
[ ] Collect required inputs (paths, constraints, desired output).
[ ] Confirm connection target, role, and timeout guardrails before running commands.
[ ] Execute the skill workflow and produce outputs.
[ ] Validate outputs and update links/backlinks if applicable.

## Testing and validation
- You must follow validation steps in the skill or linked docs.

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
- Search path, connection startup files, or role assumptions can invalidate results.
- Planner analysis and large counts may be too expensive for the active environment.

## Examples

- Example objective: "Verify a migration against a PostgreSQL staging database"
- Example validation: "`psql -X -v ON_ERROR_STOP=1 "$DATABASE_URL" -c '\conninfo'`"

## Open questions
- None.
