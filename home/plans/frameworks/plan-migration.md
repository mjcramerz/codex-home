# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-migration.md` as a runtime-pack surface and when to stop browsing.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements
- State the outcome to ship.
- You must define data-integrity and backward-compatibility requirements.
- You must define downtime, maintenance-window, and compliance constraints.

## Scope
- In: state, data, configuration, or runtime transitions that must change.
- Out: unaffected services, data, or behavior that must remain stable.

## Constraints / Non-goals
- You must record safety limits, deadlines, and explicit non-goals.

## Dependencies and assumptions
- List upstream and downstream dependencies with owners.
- You must record environment and access assumptions.
- You must record backup, restore, and audit-evidence assumptions.

## Success metrics and exit criteria
- You must define migration correctness and data-quality metrics.
- You must define runtime performance and error-budget targets after cutover.
- State go/no-go criteria and the sign-off owner.

## Current state (inventory)
- List the files, modules, or services involved.
- List the data stores, schemas, or contracts involved.
- List deployment or operational touchpoints.

## Action items
[ ] Define migration boundaries and compatibility guardrails for the affected files and services.
[ ] Implement the forward migration with bounded execution and retries.
[ ] Implement backward migration or a safe fallback path.
[ ] Add feature flags, guards, and progressive rollout controls where needed.
[ ] Execute rehearsal or dry-run in staging and capture evidence.
[ ] Update `$CODEX_HOME/docs/workflows/` and operator checklists.

## Testing and validation
- List validation commands from fastest to deepest.
- State explicit acceptance criteria for cutover and rollback.

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

## Risks / Rollback
- Describe data-safety, compatibility, and rollback risks explicitly.

## References
- List the tickets, specs, links, and files that define or approve the migration.

## Examples
- Example objective: "Migrate the runtime skill metadata contract with rollback and verification steps."
- Example validation: "python3 -m unittest tests.test_skill_catalog_contract tests.test_runtime_reference_contract"
