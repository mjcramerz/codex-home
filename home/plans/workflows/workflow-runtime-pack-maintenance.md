# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-runtime-pack-maintenance.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/runtime-pack-maintenance.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/runtime-pack-maintenance.md`
- `$CODEX_HOME/docs/instruction-system.md` for model/catalog/configuration work
- Current repo scope, constraints, and validation commands

## Scope
- In: work covered by the `runtime-pack-maintenance` workflow.
- Out: unrelated repository changes.

## Action items
[ ] Route to the workflow and confirm the smallest concrete entrypoint.
[ ] Inventory the affected sources, required mirrors, generated artifacts, and
    installed runtime outputs.
[ ] Confirm the active configuration path and model/catalog capability contract
    before changing Code Mode or instruction behavior.
[ ] Update source-managed assets first; never edit installed outputs or copy
    schema placeholder values into active configuration.
[ ] Synchronize only required mirrors and keep routing, architecture, workflow,
    plan, and manifest links in sync.
[ ] Reparse changed structured files and run the matching validator:
    `scripts/validate_model_catalogs.py`,
    `scripts/validate_runtime_pack_assets.py`, and/or
    `schemas/config_toml_coverage.py --check`.
[ ] Record evidence, known runtime limitations, rollout order, and rollback
    conditions in the handoff.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.

## Deployment checkpoints
- You must document rollout order, blast-radius controls, and rollback conditions.
- You must record any required follow-up validation owners.
