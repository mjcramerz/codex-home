---
title: Rollback and recovery for rooted Pixel 9a lab devices
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- references
- rollback-and-recovery-md
- rollback-and-recovery
- user
- security-labs
updated: '2026-02-20'
---
# Rollback and recovery for rooted Pixel 9a lab devices

## Goal
Ensure every root/flash step has a tested recovery path before progressing.

## Required rollback assets
- Original boot image for exact build fingerprint.
- Known-good factory image package.
- Fastboot host tools with verified version.
- Recovery decision log and operator contact.

## Minimum rollback drill
1) Verify device enters bootloader mode reliably.
2) Flash known-good boot image and reboot.
3) Verify Android boots and `adb` reconnects.
4) Verify critical functions: radio, Wi-Fi, camera, USB.
5) Record drill timing and any blockers.

## Failure handling
- If bootloop persists, stop and escalate to device recovery owner.
- Do not continue NetHunter validation until recovery is proven.
