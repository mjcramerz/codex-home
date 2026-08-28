---
name: infra-virsh
description: Manage libvirt and KVM virtual machines directly with virsh commands and XML-based
  domain control. Use when the user asks for virsh/libvirt operations outside Proxmox- managed
  environments.
metadata:
  version: '1.0'
  short-description: Manage libvirt/KVM workflows with virsh safely
  tags:
  - virsh
  - kvm
  - virtualization
  - infra
interface:
  display-name: INFRA-libvirt/virsh
  short-description: Manage libvirt/KVM workflows with virsh safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC56'
  default-prompt: Act as the "INFRA-libvirt/virsh" specialist for "Manage libvirt/KVM workflows
    with virsh safely". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- defining or operating libvirt domains
- automating VM lifecycle steps

## Workflow
1) Author domain XML.
2) Define and start domains.
3) Verify console and networking.

## Checkpoint gates
- Host gate: verify KVM/libvirt capabilities, storage pool availability, and network definitions before domain changes.
- XML gate: validate domain XML schema and pin critical choices (machine type, CPU mode, disk bus, NIC model); validate storage and network XML before define/start.
- Provision gate: define and start domains in reversible steps (`define` -> `start` -> `autostart`) with explicit teardown path.
- Data safety gate: separate `destroy` from `undefine` decisions and call out when disks/snapshots may be deleted.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Schema validation: run `virsh domxml-validate <domain.xml>` before `virsh define`.
- Runtime validation: confirm domain state and resources (`virsh domstate`, `virsh dominfo`, `virsh domblklist`).
- Connectivity validation: verify console/login and network assignment (`virsh console` or `virsh domifaddr`) after boot.
- Lifecycle validation: test stop/start/reboot behavior and confirm autostart, snapshot, and backup expectations.

## Outputs
- Validated domain XML plus required pool/network definitions and assumptions.
- Lifecycle command runbook (define/start/stop/reboot/destroy/undefine) with safety warnings.
- Post-provision verification checklist and rollback path for failed boots or misconfigured networking.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/scripts/skill_helper.py`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/references/domain-xml-guardrails.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/references/storage-network-playbook.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/assets/domain-template.xml`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virsh/assets/network-template.xml`

## References
- `$CODEX_HOME/docs/workflows/virsh.md`
- `$CODEX_HOME/docs/virtualization/virsh.md`
- `$CODEX_HOME/templates/virtualization/virsh-vm-skeleton/`
- `$CODEX_HOME/snippets/virsh/domain.xml`
