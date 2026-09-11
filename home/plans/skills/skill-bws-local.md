# Bws local plan

Use this plan when you applying or updating the `bws-local` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `bws-local` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `bws-local` skill only when its trigger matches this task and the skill is available.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: local BWS install/config/keyring lifecycle tasks defined by the skill.
- Out: CI/CD pipeline-level BWS integrations.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Use skill bws-local and linked resources.
- [ ] Collect required host constraints (Debian version, shell model, privilege boundaries).
- [ ] Execute the skill workflow with local-only scope.
- [ ] Validate outputs and cross-link docs/prompts/index references if changed.

## Testing and validation

- Follow validation steps in the skill or linked docs.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout/retry limits, and failure behavior for keyring and sudo operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Capture expected outcomes and acceptance criteria for each validation step.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Confirm rollout notes cover binary/path visibility and keyring read-path verification.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## Risks and edge cases

- DBus/session keyring bootstrap may differ across local shell/session types.
- PATH visibility may lag until login shell refresh.
- Root-invoked workflows can target wrong keyring user without explicit owner mapping.

## Examples

- Example objective: "Harden local bws install + keyring lifecycle for Debian workstation."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
