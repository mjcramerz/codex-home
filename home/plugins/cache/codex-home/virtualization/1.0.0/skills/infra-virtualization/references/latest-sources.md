---
title: infra-virtualization reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-virtualization
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-virtualization reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
VM-based virtualization workflows: QEMU/KVM/libvirt, Vagrant, networking modes, and reproducible dev environments.

## SKILL.md coverage checklist
- Use this skill when
- Non-negotiables
- Workflow
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Outputs
- Local resources
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virtualization/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virtualization/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/1.0.0/skills/infra-virtualization/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `networking-modes.md`
- `operations-checklist.md`
- `provider-decision-matrix.md`
- `risk-register.md`

## Context7 coverage
- `/libvirt/libvirt`
- `/vagrant-libvirt/vagrant-libvirt`

## Web verification targets
- `https://www.qemu.org/docs/master/`
- `https://developer.hashicorp.com/vagrant/docs`

## External references
- [QEMU documentation](https://www.qemu.org/docs/master/) - Hypervisor behavior, device model options, and runtime controls.
- [libvirt docs](https://libvirt.org/docs.html) - Host capability checks, network/storage primitives, and VM XML orchestration.
- [Vagrant docs](https://developer.hashicorp.com/vagrant/docs) - Reproducible VM workflow commands and provider behavior.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-virtualization` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-virtualization` before finalizing changes.
