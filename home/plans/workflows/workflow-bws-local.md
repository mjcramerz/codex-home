# Bws local plan

Use this plan when you following `$CODEX_HOME/docs/workflows/bws-local.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/bws-local.md`.

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

- [ ] Validate host prerequisites and trust boundaries for local BWS usage.
- [ ] Execute install and system PATH setup with explicit privilege boundaries.
- [ ] Store/rotate keyring entries and validate read path.
- [ ] Run install/read-path verification checks and capture non-secret evidence.

## Testing and validation

- Run workflow-defined checks for install, keyring update/status, and read-path verification.

## Security checkpoints

- Confirm token and project ID values are never printed or copied into logs/notes.
- Verify keyring service/account identifiers use constrained, expected values.
- Ensure privileged actions require explicit sudo prompts and avoid full-root execution mode.

## Testing checkpoints

- Define fast-path checks (`make check`, help output checks) before mutation steps.
- Re-run key verification commands after each state-changing operation.
- Validate negative paths (missing keyring entries, invalid identifiers, root invocation guardrails).

## Deployment checkpoints

- Roll out in deterministic order: install -> keyring update -> verification.
- Record the follow-up verification cadence for periodic token rotation and keyring read-path checks.

## Multi-agent handoff

- When coordinating, hand off host assumptions and expected final local state.
- When executing, report files touched, commands run, and non-secret verification evidence.
- Reviewer confirms local-only scope and security controls before completion.

## Risks and edge cases

- Headless DBus sessions may require explicit session bootstrap before keyring operations.
- Mixed shell startup behavior can delay PATH visibility until a new shell session.
- Root-invoked workflows can target the wrong keyring user without explicit owner mapping.

## Examples

- Example objective: "Install local bws with system PATH wiring and persist access token in keyring."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
