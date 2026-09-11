# Migration plan

Use this plan when you need to carry out migration work. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- State the outcome to ship.
- Define data-integrity and backward-compatibility requirements.
- Define downtime, maintenance-window, and compliance constraints.

## Scope

- In: state, data, configuration, or runtime transitions that must change.
- Out: unaffected services, data, or behavior that must remain stable.

## Constraints / Non-goals

- Record safety limits, deadlines, and explicit non-goals.

## Dependencies and assumptions

- List upstream and downstream dependencies with owners.
- Record environment and access assumptions.
- Record backup, restore, and audit-evidence assumptions.

## Success metrics and exit criteria

- Define migration correctness and data-quality metrics.
- Define runtime performance and error-budget targets after cutover.
- State go/no-go criteria and the sign-off owner.

## Current state (inventory)

- List the files, modules, or services involved.
- List the data stores, schemas, or contracts involved.
- List deployment or operational touchpoints.

## Action items

- [ ] Define migration boundaries and compatibility guardrails for the affected files and services.
- [ ] Implement the forward migration with bounded execution and retries.
- [ ] Implement backward migration or a safe fallback path.
- [ ] Add feature flags, guards, and progressive rollout controls where needed.
- [ ] Execute rehearsal or dry-run in staging and capture evidence.
- [ ] Update `$CODEX_HOME/docs/workflows/` and operator checklists.

## Testing and validation

- List validation commands from fastest to deepest.
- State explicit acceptance criteria for cutover and rollback.

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

## Risks / Rollback

- Describe data-safety, compatibility, and rollback risks explicitly.

## References

- List the tickets, specs, links, and files that define or approve the migration.

## Examples

- Example objective: "Migrate the runtime skill metadata contract with rollback and verification steps."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.
