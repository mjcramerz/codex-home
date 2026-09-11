# Framework plan catalog

Use this plan when you need to carry out framework plan catalog work. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use these templates when the task does not map cleanly to one workflow or one skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Choose a framework plan

<!-- BEGIN:contents -->
- `$CODEX_HOME/plans/frameworks/plan-bugfix.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-docs-and-runbook.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-feature-delivery.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-infra-change.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-integration.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-migration.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-performance.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-refactor.md` — Plan
- `$CODEX_HOME/plans/frameworks/plan-security-hardening.md` — Plan
<!-- END:contents -->

## Use these when

- you need a general plan structure fast
- the task spans several files or systems
- you need explicit rollout and validation checkpoints without a workflow-specific template

## Choose the workflow this way

- `plan-feature-delivery.md` for user-visible behavior changes
- `plan-bugfix.md` for defect reproduction and bounded fixes
- `plan-refactor.md` for behavior-preserving structural changes
- `plan-migration.md` for data, schema, or state transitions
- `plan-integration.md` for external APIs or service boundaries
- `plan-security-hardening.md` for threat-driven hardening work
- `plan-performance.md` for profiling and optimization
- `plan-infra-change.md` for service, runtime, or infrastructure changes
- `plan-docs-and-runbook.md` for documentation and operator guidance changes
