# USBGuard
Purpose: tell the Codex coding agent how to use `docs/system/usbguard.md` as a runtime-pack surface and when to stop browsing.
Guidance for USB device authorization policies.


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

## You must follow this workflow
1) Set policy to `audit` and plug trusted devices.
2) Generate a ruleset (`usbguard generate-policy`).
3) Review and reduce rules; remove broad allow entries.
4) Switch to `block` policy and validate.

## Safety notes
- You must keep an emergency TTY or console available before enforcing.
- Avoid locking out input devices on remote hosts.

See also:
- `overview.md`
- `../workflows/usbguard.md`
- `$CODEX_HOME/templates/system/usbguard-baseline/`
- `$CODEX_HOME/snippets/system/usbguard.rules`
- You must use skill secops-usbguard.
- `$CODEX_HOME/index/domains/system/hardening.md`
- `$CODEX_HOME/index/domains/system/usbguard.md`
