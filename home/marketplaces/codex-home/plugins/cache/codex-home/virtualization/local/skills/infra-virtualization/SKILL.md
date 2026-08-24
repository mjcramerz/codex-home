---
name: infra-virtualization
description: Design VM-based virtualization using QEMU/KVM/libvirt and Vagrant with reproducible
  network and storage layout. Use when the user asks for hypervisor-agnostic VM architecture
  or local VM dev environment setup.
metadata:
  version: '1.0'
  short-description: 'VM-based virtualization workflows: QEMU/KVM/libvirt, Vagrant, networking
    modes, and reproducible dev environments'
  tags:
  - virtualization
  - libvirt
  - qemu
  - kvm
  - vagrant
  - vm
  - networking
interface:
  display-name: INFRA-Virtualization
  short-description: 'VM-based virtualization workflows: QEMU/KVM/libvirt, Vagrant, networking
    modes, and reproducible dev environments'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CBCC32'
  default-prompt: 'Act as the "INFRA-Virtualization" specialist for "VM-based virtualization
    workflows: QEMU/KVM/libvirt, Vagrant, networking modes, and reproducible dev environments".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.'
---

## Use this skill when
- creating or improving VM-based dev/test environments
- documenting or configuring libvirt/QEMU/KVM
- adding Vagrant-based workflows
- choosing VM networking modes (NAT/bridged/isolated)

## Non-negotiables
- Treat host changes as high-impact; require explicit confirmation.
- Make network access explicit and document the chosen mode.
- Prefer reproducible images/boxes; avoid `latest`; pin box/image version and checksum when available.
- Provide cleanup/rollback steps.

## Workflow
1) Clarify OS target, virtualization stack, and network needs.
2) Choose the scaffold:
   - `$CODEX_HOME/templates/virtualization/vagrant-libvirt-skeleton/`
   - or `$CODEX_HOME/docs/virtualization/qemu-kvm-libvirt.md`
3) Define networking mode (NAT/bridged/isolated) and document it.
4) Pin base images/boxes and record checksums when possible.
5) Provide run and teardown commands.

## Checkpoint gates
- Host readiness gate: verify virtualization support, kernel modules, disk capacity, and required libvirt networks before provisioning.
- Image integrity gate: pin VM images/boxes and record checksum or source digest for reproducibility and rollback.
- Network gate: document NAT/bridged/isolated mode, firewall impact, and expected inbound exposure before boot.
- Deployment gate: define ordered bring-up and teardown steps (`up`, smoke checks, snapshot, destroy) with data-retention policy.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Host validation: run stack-specific checks (`virt-host-validate`, `virsh net-list --all`, provider status checks) before creating guests.
- Config validation: validate Vagrant/libvirt definitions (`vagrant validate` when available, schema/lint checks for domain XML).
- Guest validation: confirm boot, SSH/console access, provisioning success, and required service health inside the VM.
- Network validation: verify guest-to-host and guest-to-external connectivity for the chosen mode, including blocked-path expectations for isolated labs.
- Rollback validation: test snapshot restore or reprovision path before promoting the workflow for shared use.

## Outputs
- Reproducible VM definition bundle (Vagrant/libvirt config, pinned image sources, and network mode rationale).
- Deployment runbook with create, validate, snapshot, teardown, and cleanup commands.
- Verification matrix for host readiness, guest health, networking behavior, and rollback readiness.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/scripts/skill_helper.py`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/references/networking-modes.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/references/provider-decision-matrix.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/assets/Vagrantfile.template`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virtualization/assets/topology.template.yaml`

## References
- `$CODEX_HOME/docs/virtualization/overview.md`
- `$CODEX_HOME/docs/virtualization/qemu-kvm-libvirt.md`
- `$CODEX_HOME/docs/virtualization/vagrant-libvirt.md`
- `$CODEX_HOME/docs/workflows/debian-preseed.md`
- `$CODEX_HOME/templates/virtualization/vagrant-libvirt-skeleton/`
