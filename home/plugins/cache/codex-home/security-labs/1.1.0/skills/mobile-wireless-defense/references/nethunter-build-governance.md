---
title: NetHunter build governance
status: active
owner: Matthew Cramer
tags:
- skills
- all
- mobile-wireless-defense
- references
- nethunter-build-governance-md
- nethunter-build-governance
- user
- security-labs
updated: '2026-02-20'
---
# NetHunter build governance

## Objective
Keep NetHunter installer/kernel build workflows reproducible and auditable for lab use.

## Defensive checks
- pinned source revision tracking for builder and installer repos
- reproducible build logs and checksum capture
- separation of lab artifacts from production mobile infrastructure
- rollback and factory restore verification

## Upstream references
- https://www.kali.org/docs/nethunter/building-nethunter/
- https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/
- https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder
- https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer
- https://developer.android.com/tools/releases/platform-tools
