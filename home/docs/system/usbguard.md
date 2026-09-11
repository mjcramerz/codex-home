# USBGuard

Use this guide when the task concerns usbguard. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to USB device authorization policies.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/system/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Start in audit mode to collect a baseline.
- Generate rules from observed devices and prune aggressively.
- Store rules with strict permissions and version control.

## Execute the selected workflow

1. Set policy to `audit` and plug trusted devices.
2. Generate a ruleset (`usbguard generate-policy`).
3. Review and reduce rules; remove broad allow entries.
4. Switch to `block` policy and validate.

## Safety notes

- Keep an emergency TTY or console available before enforcing.
- Avoid locking out input devices on remote hosts.

See also:
- `overview.md`
- `../workflows/usbguard.md`
- `$CODEX_HOME/templates/system/usbguard-baseline/`
- `$CODEX_HOME/snippets/system/usbguard.rules`
- Read the `secops-usbguard` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/system/hardening.md`
- `$CODEX_HOME/index/domains/system/usbguard.md`
