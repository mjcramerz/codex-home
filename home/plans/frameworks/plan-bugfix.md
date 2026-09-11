# Bugfix plan

Use this plan when you are diagnosing and fixing a bug or regression. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when diagnosing and fixing a bug or regression.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Repro steps or failing test case.
- Expected vs actual behavior.
- Impact and urgency assessment.

## Scope

- In: fix, tests, and minimal supporting changes.
- Out: unrelated refactors or feature work.

## Dependencies and assumptions

- List the systems and environments required to reproduce and validate the bug.
- Record required access, logs, traces, and telemetry dependencies.

## Success metrics and exit criteria

- Reproduction no longer fails and regression coverage exists for the fixed path.
- Error rate, latency, and resource usage stay within acceptable bounds after the fix.
- Name the release-readiness owner when the bug affects shipped behavior.

## Files and entry points

- Record the reproduction entrypoints you inspected first.
- List the files or modules most likely to contain the defect.

## Action items

- [ ] Reproduce the issue and capture evidence.
- [ ] Identify root cause and affected paths.
- [ ] Design a minimal, safe fix.
- [ ] Implement the fix with guardrails.
- [ ] Add regression tests.
- [ ] Validate against repro and related cases.
- [ ] Document findings if user-facing or operational.

## Testing and validation

- List the validation commands from fastest to deepest, starting with the original repro.

## Rollout / mitigation

- Describe the rollback or mitigation path if the fix cannot ship immediately.

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

- Identify nearby behaviors, fallback paths, or configuration states that could still regress.

## Examples

- Example objective: "Fix the startup crash in the hook dispatcher when the manifest contains a malformed repo block."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- Record only the missing inputs that block reproduction or release readiness.
