---
title: Storage and network playbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-virsh
- references
- storage-network-playbook-md
- storage-network-playbook
- user
- infra
updated: '2026-02-20'
---
# Storage and network playbook

## Storage checks
- Confirm pool existence: `virsh pool-list --all`
- Confirm target volume availability before attach.
- Record backing image chain for qcow2.

## Network checks
- Confirm network definitions: `virsh net-list --all`
- Validate bridge/NAT selection against exposure requirements.
- Verify guest interface assignment after boot.

## Rollback checklist
- Detach new disks/interfaces if boot regression appears.
- Revert to previous XML snapshot copy.
- Re-test console and SSH reachability.
