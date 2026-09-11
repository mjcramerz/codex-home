# Repo ops plan

Use this plan when you applying or updating the `repo-ops` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `repo-ops` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `repo-ops` skill only when its trigger matches this task and the skill is available.
- Any referenced scripts, assets, or references in the skill

## Scope

- In: tasks covered by the `repo-ops` skill and its resources.
- Out: tasks outside the skill's domain.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Use skill repo-ops and linked resources.
- [ ] Collect required inputs (paths, constraints, desired output).
- [ ] Identify the operation type (audit, sync, release, branch promotion, or automation change) before editing.
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

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## Risks and edge cases

- Ambiguous repo state or dirty worktree invalidates the automation contract.
- Protected refs, release tags, or promotion order drift from documented policy.

## Examples

- Example objective: "Add a dry-run-safe release branch promotion helper"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
