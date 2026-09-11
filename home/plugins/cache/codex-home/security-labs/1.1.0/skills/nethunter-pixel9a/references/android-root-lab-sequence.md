---
title: Android root lab sequence (authorized device owner only)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- references
- android-root-lab-sequence-md
- android-root-lab-sequence
- user
- security-labs
updated: '2026-02-20'
---
# Android root lab sequence (authorized device owner only)

## Objective
Prepare a controlled rooted test device for NetHunter validation while preserving rollback paths.

## Sequence
1) Enable OEM unlocking + USB debugging in developer settings.
2) Confirm host tools (`adb`, `fastboot`) and trusted USB cable/port.
3) Capture and store original boot image and factory image metadata.
4) Reboot bootloader and unlock (`fastboot flashing unlock`) with user confirmation.
5) Boot Android and re-enable debugging after data wipe.
6) Patch boot image in the controlled app flow (for example via the documented Magisk process).
7) Flash patched boot image and reboot.
8) Verify root state + SafetyNet/Play Integrity impact for lab documentation.
9) Validate NetHunter prerequisites and collect evidence.
10) Execute rollback test to original boot image.

## Evidence requirements
- Command transcript with UTC timestamps.
- Input/output boot image hashes.
- Device fingerprint before and after root.
- Pass/fail matrix for root + NetHunter readiness checks.
