# GRUB workflow

Use this guide when the task concerns grub workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-grub.md` before executing this workflow.

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

1. **Scope**: target system, boot mode, kernel params.
2. **Edit**: update `/etc/default/grub`.
3. **Generate**: run `update-grub` or `grub-mkconfig`.
4. **Verify**: confirm entries and reboot with fallback.

## Safety rules

- Keep a fallback entry and recovery plan.
- Avoid removing the last working kernel.

## Security checkpoints

- Add only reviewed kernel parameters; avoid disabling required platform protections.
- Keep GRUB config files root-owned and protect write access to boot assets.
- Verify boot target disk/EFI path matches the intended host layout.

## Testing checkpoints

- Generate config with `update-grub` or `grub-mkconfig` and review resulting entries.
- Confirm fallback kernel entries remain present and bootable.
- When possible, test one-time boot selection before changing defaults.

## Deployment checkpoints

- Schedule reboot with out-of-band or local console access available.
- Keep previous config backup and explicit rollback boot instructions.
- Capture first-boot logs for bootloader or kernel parameter regressions.

## Multi-agent handoff

- Coordinator provides desired kernel args, host boot mode, and rollback constraints.
- Executor hands off config diff, generated menu evidence, and reboot outcome.
- Receiver tracks cleanup of temporary parameters after validation.
See also:
- `overview.md`
- `../system/grub.md`
- `$CODEX_HOME/templates/system/grub-baseline/`
- `$CODEX_HOME/snippets/system/grub-default`
- Read the `infra-grub` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/grub.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
