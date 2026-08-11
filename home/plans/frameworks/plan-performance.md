# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-performance.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when optimizing performance or reducing resource usage.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements
- Baseline metrics and target thresholds.
- Workloads or scenarios to optimize.

## Scope
- In: hot paths, critical workflows, and tests.
- Out: unrelated refactors or feature work.

## Dependencies and assumptions
- You must record benchmark-environment parity and workload-realism assumptions.
- You must record instrumentation, profiling access, and data-retention assumptions.

## Success metrics and exit criteria
- You must define target latency, throughput, or resource improvements.
- You must define regression guard thresholds and acceptable trade-offs.
- State the owner who approves release readiness.

## Files and entry points
- List the hot-path modules under investigation.
- List the benchmark or load-test entrypoints you will use.

## Action items
[ ] Capture baseline metrics and reproduce workloads.
[ ] Profile and identify bottlenecks.
[ ] Propose optimizations and trade-offs.
[ ] Implement minimal changes and re-measure.
[ ] Add or update performance regression guards.
[ ] Document results and tuning knobs.

## Testing and validation
- List benchmarks, load tests, and perf counters from fastest to deepest.

## Rollout / monitoring
- You must define regression alerts and any SLOs affected by the change.

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
- Call out correctness trade-offs, cache invalidation pitfalls, and measurement blind spots.

## Examples
- Example objective: "Reduce render latency for the runtime pack contract tests without changing coverage."
- Example validation: "hyperfine 'python3 -m unittest tests.test_runtime_pack_structure_contract'"

## Open questions
- You must record only the missing metrics, profilers, or environments that block the work.
