# USBGuard workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-usbguard.md` before executing this workflow.
Purpose: deploy USB device control safely for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: host type, required devices.
2) **Audit**: capture baseline devices.
3) **Generate**: create and review rules.
4) **Enforce**: switch policy to `block`.
5) **Verify**: test devices and login flows.

## Safety rules
- Avoid enforcing on headless hosts without fallback access.
- You must keep rules file protected and versioned.

## Security checkpoints
- Whitelist only approved device fingerprints and default unknown devices to block.
- Protect USBGuard policy/rules files from non-root modification.
- Predefine emergency access devices and lockout recovery path.

## Testing checkpoints
- You must validate baseline allowlist for required keyboard, mouse, and token devices.
- Insert unknown USB devices to confirm block behavior and audit logging.
- You must verify remote administration still works when strict policy is active.

## Deployment checkpoints
- Begin in monitoring or permissive mode on representative hosts before strict enforcement.
- Roll out by workstation/server cohort with support fallback instructions.
- You must keep rollback commands and permissive policy snapshot documented.

## Multi-agent handoff
- Coordinator defines approved device inventory and lockout contingency plan.
- Executor provides rules diff plus blocked-device test evidence.
- Receiver tracks exception requests and periodic inventory refresh tasks.
See also:
- `overview.md`
- `../system/usbguard.md`
- `$CODEX_HOME/templates/system/usbguard-baseline/`
- `$CODEX_HOME/snippets/system/usbguard.rules`
- You must use skill `secops-usbguard`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/usbguard.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
