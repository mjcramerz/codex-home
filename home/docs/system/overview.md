# Host hardening overview
Purpose: route OS-level boot, kernel, sysctl, optimization, and device-control work to the correct guide for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Scope
- Bootloader and kernel command-line changes
- Kernel build/config and module policy
- Sysctl tuning
- Performance/security tuning
- USB device control

## You must enforce these guardrails
- You must treat host changes as high-risk and rollback-sensitive.
- You must validate in a VM or equivalent lab when feasible.
- Make one class of change at a time and verify it before layering more.

## Quick map
- GRUB: `grub.md`
- Kernel build/config: `kernel.md`
- sysctl tuning: `sysctl.md`
- Optimizations: `optimizations.md`
- USBGuard: `usbguard.md`
