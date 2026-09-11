# Security hardening plan

Use this plan when you review authentication, authorization, trust boundaries or defensive security controls. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

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

- Record the required security tooling, telemetry, and access.
- Record policy, compliance, and approval dependencies.

## Success metrics and exit criteria

- Define risk-reduction metrics and control-coverage targets.
- Define the validation evidence required for sign-off.
- Define incident-response and rollback readiness criteria.

## Files and entry points

- List the security-sensitive boundaries under review.
- List the auth, authz, and input-validation points that must be inspected or changed.

## Action items

- [ ] Identify primary threats and abuse cases.
- [ ] Map target controls to OWASP API Top 10 and (when applicable) NISTIR 8259A baseline capabilities.
- [ ] Review current controls and gaps.
- [ ] Design mitigations (validation, auth, limits, logging).
- [ ] Implement changes with safe defaults.
- [ ] Add negative tests and regression coverage.
- [ ] Update security documentation under `$CODEX_HOME/docs/`.

## Testing and validation

- List the security tests, linters, scans, and manual review steps in execution order.

## Rollout / monitoring

- Define staged rollout, alerting, and incident-response expectations.

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

- Call out false positives, false negatives, bypass risks, and operational trade-offs.

## Examples

- Example objective: "Harden the plugin/runtime reference surfaces against stale-path regressions."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- Record only the policy or threat-model gaps that block sign-off.
