# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-security-hardening.md` as a runtime-pack surface and when to stop browsing.

Use this plan for security reviews, mitigations, and hardening changes.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements
- Threat model or risk statement.
- Security objectives and acceptance criteria.
- Compliance or policy constraints.

## Scope
- In: targeted attack surfaces and mitigations.
- Out: unrelated feature or refactor work.

- API-facing surfaces: map controls against OWASP API Security Top 10 (2023) categories.

## Dependencies and assumptions
- You must record the required security tooling, telemetry, and access.
- You must record policy, compliance, and approval dependencies.

## Success metrics and exit criteria
- You must define risk-reduction metrics and control-coverage targets.
- You must define the validation evidence required for sign-off.
- You must define incident-response and rollback readiness criteria.

## Files and entry points
- List the security-sensitive boundaries under review.
- List the auth, authz, and input-validation points that must be inspected or changed.

## Action items
[ ] Identify primary threats and abuse cases.
[ ] Map target controls to OWASP API Top 10 and (when applicable) NISTIR 8259A baseline capabilities.
[ ] Review current controls and gaps.
[ ] Design mitigations (validation, auth, limits, logging).
[ ] Implement changes with safe defaults.
[ ] Add negative tests and regression coverage.
[ ] Update security documentation under `$CODEX_HOME/docs/`.

## Testing and validation
- List the security tests, linters, scans, and manual review steps in execution order.

## Rollout / monitoring
- You must define staged rollout, alerting, and incident-response expectations.

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
- Call out false positives, false negatives, bypass risks, and operational trade-offs.

## Examples
- Example objective: "Harden the plugin/runtime reference surfaces against stale-path regressions."
- Example validation: "python3 -m unittest tests.test_runtime_reference_contract"

## Open questions
- You must record only the policy or threat-model gaps that block sign-off.
