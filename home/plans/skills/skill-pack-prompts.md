# Pack prompts plan

Use this plan when you applying or updating the `pack-prompts` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `pack-prompts` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `pack-prompts` skill only when its trigger matches this task and the skill is available.
- Prompt command scope, contract changes, and maintenance constraints.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `pack-prompts` skill and its resources.
- Out: tasks outside prompt-library maintenance.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Use skill pack-prompts and linked resources.
- [ ] Collect required inputs (commands, constraints, desired output).
- [ ] Execute the skill workflow and update prompt-maintenance assets as needed.
- [ ] Validate outputs and keep routing/index references consistent.

## Testing and validation

- Follow validation steps in the skill or linked docs.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Capture expected outcomes and acceptance criteria for each validation step.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Confirm migration/backfill or feature-flag sequencing when applicable.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## Risks and edge cases

- Prompt command contracts drift from documented maintenance assets.
- Source/runtime prompt directories diverge because sync happened before validation.

## Examples

- Example objective: "Add a slash command and wire prompt-maintenance links and checks."

## Open questions

- None.
