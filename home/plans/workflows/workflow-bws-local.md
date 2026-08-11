# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-bws-local.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/bws-local.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/bws-local.md`
- Local environment details (Debian version, shell type, sudo policy)
- Secret metadata only (`BWS_ACCESS_TOKEN` + `BWS_PROJECT_ID` presence), never secret values in planning notes

## Scope
- In: local BWS install/config/keyring lifecycle on Debian systems.
- Out: CI/CD integrations and remote pipeline secret orchestration.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Validate host prerequisites and trust boundaries for local BWS usage.
[ ] Execute install and system PATH setup with explicit privilege boundaries.
[ ] Store/rotate keyring entries and validate read path.
[ ] Run install/read-path verification checks and capture non-secret evidence.

## Testing and validation
- You must run workflow-defined checks for install, keyring update/status, and read-path verification.

## Security checkpoints
- You must confirm token and project ID values are never printed or copied into logs/notes.
- You must verify keyring service/account identifiers use constrained, expected values.
- Ensure privileged actions require explicit sudo prompts and avoid full-root execution mode.

## Testing checkpoints
- You must define fast-path checks (`make check`, help output checks) before mutation steps.
- You must re-run key verification commands after each state-changing operation.
- You must validate negative paths (missing keyring entries, invalid identifiers, root invocation guardrails).

## Deployment checkpoints
- Roll out in deterministic order: install -> keyring update -> verification.
- You must record the follow-up verification cadence for periodic token rotation and keyring read-path checks.

## Multi-agent handoff
- Coordinator hands off host assumptions and expected final local state.
- Executor reports files touched, commands run, and non-secret verification evidence.
- Reviewer confirms local-only scope and security controls before completion.

## Risks and edge cases
- Headless DBus sessions may require explicit session bootstrap before keyring operations.
- Mixed shell startup behavior can delay PATH visibility until a new shell session.
- Root-invoked workflows can target the wrong keyring user without explicit owner mapping.

## Examples

- Example objective: "Install local bws with system PATH wiring and persist access token in keyring."
- Example validation: "run the smallest local keyring, binary, and service checks that prove the lifecycle change"

## Open questions
- None.
