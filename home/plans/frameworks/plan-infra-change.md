# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-infra-change.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when modifying infrastructure, deployment, or system services.

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
- You must record network, storage, identity, and platform constraints.
- You must define the maintenance window and rollback prerequisites.

## Success metrics and exit criteria
- You must define post-change availability, reliability, and performance targets.
- You must define drift checks and policy-compliance criteria.
- State promotion go/no-go criteria and the sign-off owner.

## Files and entry points
- List the infra configs or manifests being changed.
- List the service definitions, automation entrypoints, and pipelines involved.

## Action items
[ ] Inventory current infra and dependencies.
[ ] Define desired state and compatibility constraints.
[ ] Plan rollout steps and rollback strategy.
[ ] Implement changes with least privilege and safety checks.
[ ] Update monitoring/alerts and runbooks.
[ ] Validate in staging or dry-run where possible.

## Testing and validation
- List linters, policy checks, dry-runs, and staging deploy steps in execution order.

## Rollout / migration
- Describe phased rollout order, backups, and post-change verification steps.

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
- Call out downtime, data-loss, secret-scoping, or drift risks explicitly.

## Examples
- Example objective: "Change the runtime plugin marketplace generation flow with explicit rollback steps."
- Example validation: "run the smallest syntax and unit checks that prove the infrastructure contract change"

## Open questions
- You must record only the missing approvals or environment details that block rollout.
