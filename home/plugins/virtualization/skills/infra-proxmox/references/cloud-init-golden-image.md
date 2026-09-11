---
title: Cloud-init golden image notes
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-proxmox
- references
- cloud-init-golden-image-md
- cloud-init-golden-image
- user
- infra
updated: '2026-02-20'
---

# Cloud-init golden image notes

Consult this reference when cloud-init golden image notes is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Golden image requirements

- qemu-guest-agent installed and enabled
- cloud-init package present and datasource verified
- SSH host keys regenerated on first boot
- Base template patched and rebooted before conversion

## Template validation

```bash
qm template <vmid>
qm cloudinit dump <vmid> user
```

## Clone safety

- Assign unique VMID and hostname.
- Validate bridge/VLAN assignment.
- Confirm IP addressing source (DHCP vs static cloud-init config).
