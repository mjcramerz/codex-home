# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-bugfix.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when diagnosing and fixing a bug or regression.

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
- You must record required access, logs, traces, and telemetry dependencies.

## Success metrics and exit criteria
- Reproduction no longer fails and regression coverage exists for the fixed path.
- Error rate, latency, and resource usage stay within acceptable bounds after the fix.
- Name the release-readiness owner when the bug affects shipped behavior.

## Files and entry points
- You must record the reproduction entrypoints you inspected first.
- List the files or modules most likely to contain the defect.

## Action items
[ ] Reproduce the issue and capture evidence.
[ ] Identify root cause and affected paths.
[ ] Design a minimal, safe fix.
[ ] Implement the fix with guardrails.
[ ] Add regression tests.
[ ] Validate against repro and related cases.
[ ] Document findings if user-facing or operational.

## Testing and validation
- List the validation commands from fastest to deepest, starting with the original repro.

## Rollout / mitigation
- Describe the rollback or mitigation path if the fix cannot ship immediately.

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
- Identify nearby behaviors, fallback paths, or configuration states that could still regress.

## Examples
- Example objective: "Fix the startup crash in the hook dispatcher when the manifest contains a malformed repo block."
- Example validation: "python3 -m unittest tests.test_hooks_scripts"

## Open questions
- You must record only the missing inputs that block reproduction or release readiness.
