# Aptly plan

Use this plan when you following `$CODEX_HOME/docs/workflows/aptly.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/aptly.md`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- `$CODEX_HOME/docs/workflows/aptly.md`
- Current repo scope, constraints, and validation commands

## Scope

- In: work covered by the `aptly` workflow.
- Out: unrelated repository changes.

## Action items

- [ ] Route to the workflow and confirm the smallest concrete entrypoint.
- [ ] Inventory the affected files, repos, and runtime contracts.
- [ ] Apply focused updates and keep cross-links in sync.
- [ ] Run the narrowest relevant validation and record evidence.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout or retry limits, and failure behavior for risky operations.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Record any required follow-up validation owners.
