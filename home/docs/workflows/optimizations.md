# Host optimizations workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-optimizations.md` before executing this workflow.
Purpose: apply performance/security tuning safely for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: target workload and metrics.
2) **Baseline**: capture current performance and stability.
3) **Change**: apply one tuning change.
4) **Measure**: compare results.
5) **Decide**: keep or roll back.

## Safety rules
- Avoid bundling multiple changes at once.
- You must document every knob and rationale.

## Security checkpoints
- Review each tuning knob for side effects on isolation, auth, or auditability.
- Reject opaque tuning bundles; require source, rationale, and owner for each change.
- You must require explicit approval when a performance tweak weakens safeguards.

## Testing checkpoints
- You must capture baseline metrics with fixed workload and duration before changes.
- Apply one change at a time and rerun identical benchmarks plus stability checks.
- Store benchmark scripts/results so regressions are reproducible.

## Deployment checkpoints
- Promote only changes with measurable gain and no agreed SLO regression.
- You must use canary-first rollout with hold points between host groups.
- You must document rollback value for every modified setting before rollout begins.

## Multi-agent handoff
- Coordinator sets target metrics, regression budget, and stop conditions.
- Executor provides parameter diffs, benchmark evidence, and keep/rollback decision.
- Receiver schedules periodic revalidation as workload patterns shift.
See also:
- `overview.md`
- `../system/optimizations.md`
- You must use skill `infra-optimizations`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/optimizations.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
