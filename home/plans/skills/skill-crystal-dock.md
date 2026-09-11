# Crystal dock plan

Use this plan when you applying or updating the `crystal-dock` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `crystal-dock` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `crystal-dock` skill only when its trigger matches this task and the skill is available.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `crystal-dock` skill and its resources.
- Out: tasks outside the skill’s domain.

## Action items

- [ ] Use skill `crystal-dock` and linked resources.
- [ ] Collect required inputs (paths, constraints, desired output).
- [ ] Confirm dock command source, PID-file path, and session-owner expectations.
- [ ] Execute the skill workflow and produce outputs.
- [ ] Validate outputs and update links/backlinks if applicable.

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
