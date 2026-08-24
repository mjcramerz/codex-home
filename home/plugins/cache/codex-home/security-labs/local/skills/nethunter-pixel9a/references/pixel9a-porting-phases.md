---
title: Pixel 9a NetHunter porting phases
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- references
- pixel9a-porting-phases-md
- pixel9a-porting-phases
- user
- security-labs
updated: '2026-02-20'
---
# Pixel 9a NetHunter porting phases

## Objective
Port NetHunter kernel support onto a Google Pixel 9a baseline in a reproducible, auditable lab process.

## Phase 1: Baseline capture
1) Capture device identity and build baseline.
2) Record Android version, build fingerprint, boot slot, and patch level.
3) Confirm bootloader state and backup status.

## Phase 2: Source alignment
1) Map device codename from `adb shell getprop ro.product.device`.
2) Select matching Google kernel source branch/tag for the captured build line.
3) Record source commit IDs and toolchain versions in evidence log.

## Phase 3: Port branch preparation
1) Create dedicated `mcr/feature/nethunter-pixel9a-*` branch in your working repo.
2) Add or update NetHunter device profile entries in the kernels data set.
3) Create a minimal `local.config` override for builder settings.

## Phase 4: Kernel patch and build
1) Apply patch sets in small reviewable commits.
2) Build with deterministic environment variables and pinned toolchains.
3) Capture build logs, output hashes, and artifact manifest.

## Phase 5: Installer package build
1) Initialize installer kernels metadata (`./bootstrap.sh`) if missing.
2) Build installer zip with explicit Android version flag.
3) Validate output contents and hashes.

## Phase 6: Lab flash + verification
1) Flash only the documented lab device.
2) Verify boot stability, Wi-Fi, USB OTG/HID, and NetHunter app function.
3) Capture regressions and decide keep/rollback.
