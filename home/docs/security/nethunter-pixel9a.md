# NetHunter Pixel 9a reference
Purpose: tell the Codex coding agent how to use `docs/security/nethunter-pixel9a.md` as a runtime-pack surface and when to stop browsing.

This guide supports repeatable Pixel 9a NetHunter work with explicit scope, evidence, and rollback guardrails.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Mission
Run a governed, reproducible Pixel 9a NetHunter kernel-porting + root validation program with:
- documented scope boundaries,
- deterministic build/flash evidence,
- rollback-ready device recovery.

## Source baseline (authoritative)
- Kali NetHunter docs: building + porting + kernel-builder workflows.
- Android official docs: bootloader locking/unlocking, fastbootd, GKI release guidance.
- Android Platform-Tools release notes for `adb`/`fastboot` compatibility.

## Current refresh snapshot (2026-02-13 UTC)
- Kali `building-nethunter` and `porting-nethunter-kernel-builder` docs show `Updated on: 2025-Jun-18`.
- Android lock/unlock and fastbootd docs show `Last updated 2025-12-02 UTC`.
- Android Platform-Tools page shows `Last updated 2026-02-10 UTC`; latest listed release is `35.0.2 (July 2024)`.
- AOSP GKI release-process page shows `Last updated 2026-01-14 UTC`.

## Required guardrails
- Scope manifest (`workflow = "nethunter-pixel9a"`, declared device IDs, and a non-expired `expires_utc`).
- Organization-owned lab device only.
- Stock factory image + stock boot image captured before unlock/flash.
- Known rollback sequence tested before operational validation.

## Phase 0: Scope and host preflight
1) Validate scope with `nethunter_scope_guard.py`.
2) Verify host tools and versions (record outputs in evidence bundle):
```bash
adb version
fastboot --version
git --version
python3 --version
```
3) Validate host can see the expected lab device:
```bash
adb devices -l
fastboot devices
```
4) Capture host + operator metadata in an evidence directory.

## Phase 1: Device baseline capture
```bash
adb devices -l
adb shell getprop ro.product.device
adb shell getprop ro.build.fingerprint
adb shell getprop ro.build.version.release
adb shell getprop ro.build.version.security_patch
adb shell getprop ro.boot.slot_suffix
adb shell getprop ro.boot.flash.locked
adb shell getprop ro.boot.verifiedbootstate
fastboot getvar current-slot
fastboot getvar is-userspace
```

Expected stop conditions in this phase:
- Device fingerprint or codename does not match the documented scope.
- Bootloader state is unexpected for planned operation window.
- Baseline evidence is incomplete (cannot prove pre-change state).

## Phase 2: Source alignment strategy
Use the device fingerprint and Android major version to align Google kernel and NetHunter inputs.

Recommended approach:
1) Record baseline branch/tag for Google kernel source.
2) Record NetHunter builder and installer commit IDs.
3) Keep one checkpoint log per porting campaign and land authored edits on `mcr/main` only.
4) Group commits by concern:
   - source/build fixes,
   - NetHunter-specific feature enablement,
   - device validation fixes.
5) Keep a one-page mapping table:
   - captured fingerprint,
   - selected Google kernel branch/tag,
   - selected NetHunter builder commit,
   - selected NetHunter installer commit,
   - rationale and reviewer sign-off.

## Phase 3: Prepare NetHunter build repositories
```bash
export NH_KERNEL_BUILDER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder.git"
export NH_INSTALLER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer.git"

git clone "$NH_KERNEL_BUILDER_REPO_URL"
git clone "$NH_INSTALLER_REPO_URL"

cd kali-nethunter-kernel-builder
cp config local.config
# Keep only required, minimal overrides in local.config

cd ../kali-nethunter-installer
./bootstrap.sh
./build.py -h
```

## Phase 4: Build controls and evidence
For each build attempt, capture:
- builder commit ID,
- installer commit ID,
- `local.config` hash,
- build log path,
- artifact hashes.

Example evidence commands:
```bash
git -C kali-nethunter-kernel-builder rev-parse HEAD
git -C kali-nethunter-installer rev-parse HEAD
sha256sum kali-nethunter-kernel-builder/local.config
```

## Phase 5: Rooting + flashing (lab device owner only)
1) Enable OEM unlock + USB debugging.
2) Reboot bootloader: `adb reboot bootloader`.
3) Unlock bootloader with explicit owner acknowledgement: `fastboot flashing unlock`.
4) Reboot and re-enable debugging after wipe.
5) Patch boot image in the documented lab flow.
6) Verify mode and slot before flashing:
   - `fastboot getvar is-userspace`
   - `fastboot getvar current-slot`
7) Flash patched boot image to explicitly selected slot and record that slot in evidence.

Slot-aware flash pattern:
```bash
fastboot getvar current-slot
fastboot flash boot_a <patched-boot.img>
fastboot reboot
```

## Phase 6: Validation matrix
Minimum post-flash checks:
- Boot stability: cold boot and reboot success.
- Control-plane: `adb` reconnect, root shell behavior.
- Connectivity: Wi-Fi, cellular/modem, Bluetooth.
- Peripheral/security features: USB OTG/HID behavior, logging telemetry intact.
- NetHunter readiness: installer/chroot/app baseline checks.
- Integrity and rollback readiness: known-good stock boot image hash matches pre-change record.

## Phase 7: Rollback drill
Run rollback on same slot with known-good stock boot image:
```bash
adb reboot bootloader
fastboot flash boot_a <stock-boot.img>
fastboot reboot
```
Success criteria:
- device boots cleanly,
- critical radios/functions restored,
- no unresolved bootloop state.

## Deliverables
- Scope validation record + scope ID.
- Build and flash transcript with UTC timestamps.
- Artifact manifest (inputs, outputs, hashes).
- Validation matrix and rollback outcome.
- Residual risk list with owner + re-test date.

Recommended evidence layout:
- `evidence/<run-id>/scope/`
- `evidence/<run-id>/baseline/`
- `evidence/<run-id>/build/`
- `evidence/<run-id>/flash/`
- `evidence/<run-id>/validation/`
- `evidence/<run-id>/rollback/`

## After that, you must check related files
- `security-labs-index.md`
- `security-labs-tool-guides.md`
- `security-labs-repo-catalog.md`
- `../workflows/nethunter-pixel9a.md`
- `$CODEX_HOME/templates/system/nethunter-pixel9a-kit/overview.md`
- You must use skill `nethunter-pixel9a`.
