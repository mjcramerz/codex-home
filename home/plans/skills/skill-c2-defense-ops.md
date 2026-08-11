# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-c2-defense-ops.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `c2-defense-ops` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill c2-defense-ops.
- Any referenced scripts, assets, or references in the skill

## Scope
- In: tasks covered by the `c2-defense-ops` skill and its resources.
- Out: out-of-scope C2 emulation or offensive activity outside the documented scope.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Use skill c2-defense-ops and linked resources.
[ ] Validate documented scope and operation class before simulation.
[ ] Execute workflow steps and produce evidence-backed outputs.
[ ] Validate outputs and update linked docs/snippets/templates if needed.

## Testing and validation
- You must follow validation steps in the skill or linked docs.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- You must record any documented exception, owner, and expiry before proceeding.

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
- Missing telemetry needed for high-confidence C2 detection validation.
- Scope mismatch between documented targets and tested infrastructure.

## Examples

- Example objective: "Apply the c2-defense-ops skill to the scoped repository task with explicit validation evidence."
- Example validation: "Run the skill's narrowest validation command plus the relevant pack contract tests."

## Open questions
- None.
