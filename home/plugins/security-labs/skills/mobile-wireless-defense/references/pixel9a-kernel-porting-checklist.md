---
title: Pixel 9a NetHunter kernel porting checklist
status: active
owner: Matthew Cramer
tags:
- skills
- all
- mobile-wireless-defense
- references
- pixel9a-kernel-porting-checklist-md
- pixel9a-kernel-porting-checklist
- user
- security-labs
updated: '2026-02-20'
---
# Pixel 9a NetHunter kernel porting checklist

## Objective
Track a controlled kernel-porting process from Google source baseline to test image validation.

## Checklist
1) Capture upstream source revision and kernel config baseline.
2) Align bootloader/slot model and Android major release assumptions.
3) Apply NetHunter patches in reviewable batches.
4) Build with deterministic toolchain settings.
5) Validate boot, modem, Wi-Fi, Bluetooth, and USB behavior in lab.
6) Record regressions and maintain rollback image for each build.

## Upstream references
- https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/
- https://www.kali.org/docs/nethunter/porting-nethunter/
- https://source.android.com/docs/core/architecture/bootloader/locking_unlocking
- https://source.android.com/docs/core/architecture/bootloader/fastbootd
- https://source.android.com/docs/core/architecture/kernel/gki-releases
