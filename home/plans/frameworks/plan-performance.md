# Performance plan

Use this plan when you are optimizing performance or reducing resource usage. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when optimizing performance or reducing resource usage.

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

- Record benchmark-environment parity and workload-realism assumptions.
- Record instrumentation, profiling access, and data-retention assumptions.

## Success metrics and exit criteria

- Define target latency, throughput, or resource improvements.
- Define regression guard thresholds and acceptable trade-offs.
- State the owner who approves release readiness.

## Files and entry points

- List the hot-path modules under investigation.
- List the benchmark or load-test entrypoints you will use.

## Action items

- [ ] Capture baseline metrics and reproduce workloads.
- [ ] Profile and identify bottlenecks.
- [ ] Propose optimizations and trade-offs.
- [ ] Implement minimal changes and re-measure.
- [ ] Add or update performance regression guards.
- [ ] Document results and tuning knobs.

## Testing and validation

- List benchmarks, load tests, and perf counters from fastest to deepest.

## Rollout / monitoring

- Define regression alerts and any SLOs affected by the change.

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

- Call out correctness trade-offs, cache invalidation pitfalls, and measurement blind spots.

## Examples

- Example objective: "Reduce render latency for the runtime pack contract tests without changing coverage."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- Record only the missing metrics, profilers, or environments that block the work.
