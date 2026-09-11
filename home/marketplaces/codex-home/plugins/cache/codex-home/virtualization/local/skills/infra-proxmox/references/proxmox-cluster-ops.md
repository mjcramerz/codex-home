---
title: Proxmox cluster operations guide
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-proxmox
- references
- proxmox-cluster-ops-md
- proxmox-cluster-ops
- user
- infra
updated: '2026-02-20'
---

# Proxmox cluster operations guide

Consult this reference when proxmox cluster operations guide is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Pre-change checks

- `pvecm status` is healthy and quorum is intact.
- Target node has sufficient storage and memory headroom.
- Backup or snapshot strategy exists for affected VMIDs.

## Safe mutation order

1. Clone/create VM
2. Apply hardware and cloud-init config
3. Validate network and storage mapping
4. Start guest and run readiness checks
5. Enable backup/autostart policy only after validation

## Failure handling

- Stop failed guest: `qm stop <vmid>`
- Preserve evidence: `qm config <vmid>`, recent task logs
- Remove only with explicit approval: `qm destroy <vmid> --purge 1`
