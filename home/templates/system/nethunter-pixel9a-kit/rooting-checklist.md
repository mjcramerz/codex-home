# Rooting and flash checklist (Pixel 9a lab)
Purpose: tell the Codex coding agent how to use `templates/system/nethunter-pixel9a-kit/rooting-checklist.md` as a runtime-pack surface and when to stop browsing.

## Preflight
- [ ] Scope file validated by `nethunter_scope_guard.py`
- [ ] Device ownership and scope confirmed
- [ ] Factory image + stock boot image available
- [ ] Host tools verified (`adb`, `fastboot`, `sha256sum`)
- [ ] Platform-Tools version captured in run notes
- [ ] Baseline captured (`fingerprint`, `security_patch`, `slot`, `lock_state`, `verifiedbootstate`)

## Root and flash sequence
- [ ] OEM unlock + USB debugging enabled
- [ ] Bootloader unlock acknowledged and executed
- [ ] Post-unlock baseline captured
- [ ] Boot image patched and hash recorded
- [ ] Current mode verified (`fastboot getvar is-userspace`)
- [ ] Target slot verified (`fastboot getvar current-slot`)
- [ ] Patched boot flashed to selected slot
- [ ] Device rebooted and root state verified

## Validation
- [ ] Android boot stability verified
- [ ] Radio/Wi-Fi/USB checks pass
- [ ] NetHunter components smoke-tested
- [ ] Evidence bundle complete (logs + hashes)
- [ ] Residual risks and follow-up tests logged with owner/date

## Rollback
- [ ] Stock boot image flashed successfully
- [ ] Device returns to known-good state
- [ ] Rollback results documented
