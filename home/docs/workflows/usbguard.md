# USBGuard workflow

Use this guide when the task concerns usbguard workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-usbguard.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Scope**: host type, required devices.
2. **Audit**: capture baseline devices.
3. **Generate**: create and review rules.
4. **Enforce**: switch policy to `block`.
5. **Verify**: test devices and login flows.

## Safety rules

- Avoid enforcing on headless hosts without fallback access.
- Keep rules file protected and versioned.

## Security checkpoints

- Whitelist only approved device fingerprints and default unknown devices to block.
- Protect USBGuard policy/rules files from non-root modification.
- Predefine emergency access devices and lockout recovery path.

## Testing checkpoints

- Validate baseline allowlist for required keyboard, mouse, and token devices.
- Insert unknown USB devices to confirm block behavior and audit logging.
- Verify remote administration still works when strict policy is active.

## Deployment checkpoints

- Begin in monitoring or permissive mode on representative hosts before strict enforcement.
- Roll out by workstation/server cohort with support fallback instructions.
- Keep rollback commands and permissive policy snapshot documented.

## Multi-agent handoff

- Coordinator defines approved device inventory and lockout contingency plan.
- When executing, provide rules diff plus blocked-device test evidence.
- Receiver tracks exception requests and periodic inventory refresh tasks.
See also:
- `overview.md`
- `../system/usbguard.md`
- `$CODEX_HOME/templates/system/usbguard-baseline/`
- `$CODEX_HOME/snippets/system/usbguard.rules`
- Read the `secops-usbguard` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/usbguard.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
