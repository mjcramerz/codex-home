# Integration plan

Use this plan when you are integrating with external APIs, SDKs, or services. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when integrating with external APIs, SDKs, or services.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- API/spec details, auth requirements, and rate limits.
- Data contracts and error handling expectations.
- Security/privacy requirements.

## Scope

- In: integration surface, adapters, and tests.
- Out: unrelated feature work.

## Dependencies and assumptions

- Record provider SLAs, ownership contacts, and escalation paths.
- Record credentials, scopes, network constraints, and environment-parity assumptions.
- Record upstream versioning, deprecation windows, and release-cadence assumptions.

## Files and entry points

- List the integration entrypoints that will change.
- Describe the config and secret-handling surfaces involved.

## Data model / API changes

- Describe new schemas, DTOs, or configuration objects that the integration introduces.

## API contract and compatibility

- Name the OpenAPI or JSON schema source and the locked version used for planning.
- Define operation mappings, success/error responses, and pagination behavior.
- Define backward-compatibility, version negotiation, and deprecation handling.
- Define server URLs, security schemes/scopes, and callback or webhook contracts where applicable.
- Define timeout budgets, retry/backoff ceilings, circuit-breaker thresholds, and dead-letter handling.

## Success metrics and exit criteria

- Define latency, error-rate, and reliability targets.
- Define functional completion criteria for every required endpoint flow.
- State the fallback path, go/no-go criteria, and sign-off owner.

## Action items

- [ ] Review provider API docs/spec and identify required endpoints.
- [ ] Capture contract-first interface (OpenAPI/JSON schema) and compatibility constraints.
- [ ] Define auth/scopes, secret rotation expectations, and quota/rate-limit posture.
- [ ] Define normalized error model (for example RFC 9457 Problem Details) and cross-system error mapping.
- [ ] Define timeout, retry, and backoff policy with idempotency handling for retried writes.
- [ ] Design integration boundary, fallback behavior, and error normalization model.
- [ ] Implement adapters/clients with strict validation at trust boundaries.
- [ ] Add tests (mocked, contract, sandbox) plus negative and resiliency scenarios.
- [ ] Define observability (logs/metrics/traces/alerts) and operational ownership.
- [ ] Document configuration, incident handling, and rollback runbook.

## Testing and validation

- List validation commands from fastest to deepest.
- Describe sandbox or mock validation steps.
- Describe contract validation against the chosen OpenAPI or JSON schema source.
- Describe failure-mode validation for dependency outages and partial failures.
- Describe offline or reconnect validation for constrained environments when relevant.

## Rollout / monitoring

- Define feature flags, canary scope, metrics, and alerts.
- Define the kill switch, fallback mode, and the decision owner.

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

- Call out rate-limit exhaustion, partial failures, data drift, auth-scope drift, and replay or idempotency risks.

## Examples

- Example objective: "Integrate the runtime pack with a remote metadata service using explicit retry and rollback rules."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- Record only the missing API details, credentials, or environment access that block delivery.
