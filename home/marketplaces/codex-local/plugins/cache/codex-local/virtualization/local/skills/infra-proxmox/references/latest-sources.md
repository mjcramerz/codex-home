---
title: infra-proxmox reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-proxmox
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-proxmox reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Plan Proxmox VM workflows with storage and network safety.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Outputs
- Local resources
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/virtualization/local/skills/infra-proxmox/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/virtualization/local/skills/infra-proxmox/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-local/virtualization/local/skills/infra-proxmox/scripts/skill_helper.py`

## Reference files in this directory
- `cloud-init-golden-image.md`
- `latest-sources.md`
- `operations-checklist.md`
- `proxmox-cluster-ops.md`
- `risk-register.md`

## Context7 coverage
- `/websites/pve_proxmox_pve-docs`

## Web verification targets
- `https://pve.proxmox.com/pve-docs/chapter-qm.html`
- `https://pve.proxmox.com/pve-docs/chapter-pvecm.html`

## External references
- [Proxmox VE QEMU VM docs](https://pve.proxmox.com/pve-docs/chapter-qm.html) - VM provisioning, cloud-init, and runtime configuration controls.
- [Proxmox cluster manager docs](https://pve.proxmox.com/pve-docs/chapter-pvecm.html) - Cluster quorum and operational safety requirements.
- [Proxmox vzdump docs](https://pve.proxmox.com/pve-docs/chapter-vzdump.html) - Backup/restore behavior and rollback-ready backup strategy.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-proxmox` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-proxmox` before finalizing changes.
