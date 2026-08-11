# GRUB workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-grub.md` before executing this workflow.
Purpose: edit GRUB configuration safely and reproducibly for the Codex coding agent.
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
1) **Scope**: target system, boot mode, kernel params.
2) **Edit**: update `/etc/default/grub`.
3) **Generate**: run `update-grub` or `grub-mkconfig`.
4) **Verify**: confirm entries and reboot with fallback.

## Safety rules
- You must keep a fallback entry and recovery plan.
- Avoid removing the last working kernel.

## Security checkpoints
- You must add only reviewed kernel parameters; avoid disabling required platform protections.
- You must keep GRUB config files root-owned and protect write access to boot assets.
- You must verify boot target disk/EFI path matches the intended host layout.

## Testing checkpoints
- Generate config with `update-grub` or `grub-mkconfig` and review resulting entries.
- You must confirm fallback kernel entries remain present and bootable.
- When possible, test one-time boot selection before changing defaults.

## Deployment checkpoints
- Schedule reboot with out-of-band or local console access available.
- You must keep previous config backup and explicit rollback boot instructions.
- You must capture first-boot logs for bootloader or kernel parameter regressions.

## Multi-agent handoff
- Coordinator provides desired kernel args, host boot mode, and rollback constraints.
- Executor hands off config diff, generated menu evidence, and reboot outcome.
- Receiver tracks cleanup of temporary parameters after validation.
See also:
- `overview.md`
- `../system/grub.md`
- `$CODEX_HOME/templates/system/grub-baseline/`
- `$CODEX_HOME/snippets/system/grub-default`
- You must use skill `infra-grub`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/grub.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
