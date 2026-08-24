---
title: infra-virsh reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-virsh
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-virsh reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Manage libvirt/KVM workflows with virsh safely.

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
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virsh/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virsh/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/virtualization/local/skills/infra-virsh/scripts/skill_helper.py`

## Reference files in this directory
- `domain-xml-guardrails.md`
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`
- `storage-network-playbook.md`

## Context7 coverage
- `/libvirt/libvirt`

## Web verification targets
- `https://www.libvirt.org/manpages/virsh.html`
- `https://libvirt.org/formatdomain.html`

## External references
- [libvirt virsh man page](https://www.libvirt.org/manpages/virsh.html) - Lifecycle commands, validation options, and state transitions.
- [libvirt domain XML format](https://libvirt.org/formatdomain.html) - Authoritative domain XML schema and device modeling behavior.
- [libvirt storage pools](https://libvirt.org/storage.html) - Storage pool/volume lifecycle semantics and safety constraints.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-virsh` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-virsh` before finalizing changes.
