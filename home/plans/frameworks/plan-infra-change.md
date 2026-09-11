# Infra change plan

Use this plan when you modifying infrastructure, deployment, or system services. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when modifying infrastructure, deployment, or system services.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Environment targets and constraints.
- Rollback requirements and downtime limits.
- Ownership and approvals (if required).

## Scope

- In: infra code, configs, services, and runbooks.
- Out: unrelated product feature changes.

## Dependencies and assumptions

- Identify the target environments, ownership boundaries, and required approvals.
- Record network, storage, identity, and platform constraints.
- Define the maintenance window and rollback prerequisites.

## Success metrics and exit criteria

- Define post-change availability, reliability, and performance targets.
- Define drift checks and policy-compliance criteria.
- State promotion go/no-go criteria and the sign-off owner.

## Files and entry points

- List the infra configs or manifests being changed.
- List the service definitions, automation entrypoints, and pipelines involved.

## Action items

- [ ] Inventory current infra and dependencies.
- [ ] Define desired state and compatibility constraints.
- [ ] Plan rollout steps and rollback strategy.
- [ ] Implement changes with least privilege and safety checks.
- [ ] Update monitoring/alerts and runbooks.
- [ ] Validate in staging or dry-run where possible.

## Testing and validation

- List linters, policy checks, dry-runs, and staging deploy steps in execution order.

## Rollout / migration

- Describe phased rollout order, backups, and post-change verification steps.

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

- Call out downtime, data-loss, secret-scoping, or drift risks explicitly.

## Examples

- Example objective: "Change the runtime plugin marketplace generation flow with explicit rollback steps."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- Record only the missing approvals or environment details that block rollout.
