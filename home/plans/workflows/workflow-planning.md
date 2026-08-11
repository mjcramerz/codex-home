# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-planning.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/planning.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/planning.md`
- External planning references when needed:
  - Microsoft PoC guidance: https://learn.microsoft.com/en-us/azure/app-modernization-guidance/launch/build-a-proof-of-concept
  - Microsoft Synapse PoC playbook: https://learn.microsoft.com/en-us/azure/synapse-analytics/guidance/proof-of-concept-playbook-dedicated-sql-pool
  - Microsoft API design guidance: https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
  - OpenAPI specification v3.2.0: https://spec.openapis.org/oas/v3.2.0.html
  - RFC 9457 Problem Details for HTTP APIs: https://datatracker.ietf.org/doc/rfc9457/
  - AWS Well-Architected implementation guidance: https://docs.aws.amazon.com/wellarchitected/latest/userguide/implement-and-track-improvements.html
  - OWASP API Security Top 10 (2023): https://owasp.org/API-Security/editions/2023/en/0x00-header/
  - CISA Secure by Design guidance: https://www.cisa.gov/securebydesign
  - systemd service execution hardening reference: https://www.freedesktop.org/software/systemd/man/systemd.exec.html

## Scope
- In: steps defined in the `planning` workflow.
- Out: unrelated workflows or tooling.

## Plan track selection
- PoC track: timeboxed hypothesis validation with explicit go/no-go criteria.
- Integration/API track: contract-first API planning with reliability/security/observability checkpoints.
- Implementation track: phased production rollout with owners, evidence, and rollback criteria.

## Success metrics and exit criteria
- <objective outcomes and measurable targets>
- <required validation evidence for plan acceptance>
- <decision owner and go/no-go criteria>

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Read `$CODEX_HOME/docs/workflows/planning.md` and related references.
[ ] Collect required inputs and constraints.
[ ] Select the plan track (PoC, integration/API, implementation) for the task.
[ ] Define measurable success metrics and go/no-go criteria.
[ ] Execute the workflow steps in order.
[ ] Validate outputs and document results.

## Testing and validation
- You must run validation steps specified by the workflow.

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
- Missing prerequisites or environment constraints.
- Workflow steps out of order for current context.

## Examples

- Example objective: "Execute the planning workflow for the current repository scope."
- Example validation: "Run the workflow's fast-path checks first, then the deeper verification commands if the risk profile requires them."

## Open questions
- None.
