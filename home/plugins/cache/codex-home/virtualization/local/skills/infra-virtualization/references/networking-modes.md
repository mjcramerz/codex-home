---
title: Virtualization networking modes
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-virtualization
- references
- networking-modes-md
- networking-modes
- user
- infra
updated: '2026-02-20'
---
# Virtualization networking modes

## Modes
- NAT: safest default for local development.
- Bridged: required when guests must be first-class LAN participants.
- Isolated/internal: safest for malware analysis or offline labs.

## Validation
- Verify expected ingress/egress for each mode.
- Check firewall and route impacts on host and guest.
- Confirm DNS and time sync behavior in constrained modes.

## Rollback
- Keep original network definitions versioned.
- Provide teardown commands for temporary networks and bridges.
