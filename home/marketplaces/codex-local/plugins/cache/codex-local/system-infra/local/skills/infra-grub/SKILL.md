---
name: infra-grub
description: Modify GRUB bootloader configuration and kernel parameters with rollback-aware
  safety checks. Use when the user asks to change boot entries, kernel args, or GRUB defaults.
metadata:
  version: '1.0'
  short-description: Safely modify GRUB configuration and kernel parameters
  tags:
  - grub
  - bootloader
  - linux
  - system
interface:
  display-name: INFRA-GRUB
  short-description: Safely modify GRUB configuration and kernel parameters
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#5E32CC'
  default-prompt: Act as the "INFRA-GRUB" specialist for "Safely modify GRUB configuration
    and kernel parameters". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- editing `/etc/default/grub`
- changing kernel command line parameters

## Workflow
1) Scope changes and rollback plan
2) Apply minimal edits
3) Regenerate GRUB config
4) Verify boot entries

## Checkpoint gates
- Pre-change: capture `/etc/default/grub`, active cmdline (`/proc/cmdline`), and current default entry (`grub-editenv list`) before edits.
- Build gate: render updated config with the distro-specific generator command (`update-grub` or `grub2-mkconfig`) and fail on syntax/path errors; confirm target output path (`/boot/grub*/grub.cfg`) before overwriting.
- Boot safety gate: keep at least one known-good kernel entry and avoid changing default entry behavior unless explicitly requested.
- Rollback gate: keep a tested restore command for `/etc/default/grub` and regenerated `grub.cfg` before scheduling reboot.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Config validation: confirm edited `GRUB_CMDLINE_LINUX*` values are quoted correctly and parameters are not duplicated or mutually exclusive.
- Generation validation: regenerate GRUB config and inspect resulting menu entries/command line values in the generated file.
- Reboot validation: after reboot, verify with `cat /proc/cmdline` and `grub-editenv list`; collect boot logs when kernel parameters affect startup.
- Recovery validation: provide explicit fallback steps for boot failure (select previous entry, restore backup, regenerate config).

## Outputs
- Minimal `/etc/default/grub` patch plus distro-correct regenerate command.
- Reboot runbook with pre-reboot checks, post-reboot verification commands, and fallback entry guidance.
- Rollback instructions referencing backup paths and commands to restore a known-good boot config.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-grub/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-grub/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-grub/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-grub/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-grub/scripts/skill_helper.py`

## References
- `$CODEX_HOME/index/domains/system/grub.md`
- `$CODEX_HOME/docs/system/grub.md`
- `$CODEX_HOME/docs/workflows/grub.md`
- `$CODEX_HOME/templates/system/grub-baseline/`
- `$CODEX_HOME/snippets/system/grub-default`
