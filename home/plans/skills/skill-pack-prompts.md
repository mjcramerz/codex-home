# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-pack-prompts.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `pack-prompts` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill pack-prompts.
- Prompt command scope, contract changes, and maintenance constraints.
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `pack-prompts` skill and its resources.
- Out: tasks outside prompt-library maintenance.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Use skill pack-prompts and linked resources.
[ ] Collect required inputs (commands, constraints, desired output).
[ ] Execute the skill workflow and update prompt-maintenance assets as needed.
[ ] Validate outputs and keep routing/index references consistent.

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
- Prompt command contracts drift from documented maintenance assets.
- Source/runtime prompt directories diverge because sync happened before validation.

## Examples

- Example objective: "Add a slash command and wire prompt-maintenance links and checks."

## Open questions
- None.
