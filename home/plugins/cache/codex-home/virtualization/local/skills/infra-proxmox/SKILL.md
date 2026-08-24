---
name: infra-proxmox
description: Operate Proxmox VE virtual machines, storage, and networking with cluster-safe
  procedures. Use when the user asks for Proxmox-specific VM tasks rather than generic libvirt
  tooling.
metadata:
  version: '1.0'
  short-description: Plan Proxmox VM workflows with storage and network safety
  tags:
  - proxmox
  - virtualization
  - infra
interface:
  display-name: INFRA-Proxmox
  short-description: Plan Proxmox VM workflows with storage and network safety
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC7A32'
  default-prompt: Act as the "INFRA-Proxmox" specialist for "Plan Proxmox VM workflows with
    storage and network safety". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- provisioning or updating Proxmox VMs
- planning storage layouts

## Workflow
1) Scope storage backend and backups.
2) Use templates + cloud-init.
3) Verify network and storage after provisioning.

## Checkpoint gates
- Storage gate: verify target datastore free space, thin/thick policy, and backup/snapshot compatibility before provisioning.
- Network gate: confirm bridge/VLAN mapping and IP allocation plan to avoid collisions or unintended external exposure.
- Template gate: require pinned template/image ID, cloud-init seed values, and guest-agent expectations before clone/create; verify snippet storage visibility on every target node.
- Deployment gate: provision in a non-destructive sequence (`qm create/clone` -> config -> start) with explicit rollback (`qm stop`/`qm destroy`) path.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Host validation: run `pvesm status`, `qm config <vmid>`, and `qm status <vmid>` to confirm storage, hardware profile, and runtime state.
- Cloud-init validation: inspect generated cloud-init payload (`qm cloudinit dump <vmid> user`) before first boot.
- Connectivity validation: verify guest networking, SSH/console access, and time sync after boot.
- Protection validation: confirm backup job/snapshot strategy, VM protection flag, and boot order before handoff to production workloads.

## Outputs
- VM specification sheet (VMID, CPU, memory, disk, datastore, bridge/VLAN, cloud-init source).
- Provisioning and rollback command sequence with required order and safety checks.
- Post-boot validation checklist including networking, guest agent, and backup readiness evidence.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/scripts/skill_helper.py`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/references/cloud-init-golden-image.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/references/proxmox-cluster-ops.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/assets/cloud-init-user-data.template.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-proxmox/assets/vm-spec.template.yaml`

## References
- `$CODEX_HOME/docs/workflows/proxmox.md`
- `$CODEX_HOME/docs/virtualization/proxmox.md`
- `$CODEX_HOME/templates/virtualization/proxmox-vm-skeleton/`
- `$CODEX_HOME/snippets/proxmox/storage.cfg`
