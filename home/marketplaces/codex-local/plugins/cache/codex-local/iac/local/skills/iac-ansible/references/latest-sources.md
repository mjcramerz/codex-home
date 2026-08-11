---
title: iac-ansible reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- iac-ansible
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-20'
---
# iac-ansible reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Build idempotent Ansible playbooks and roles safely.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-ansible/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-ansible/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-ansible/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## External references
- [Ansible documentation](https://docs.ansible.com/) - Automation and idempotent provisioning patterns.
- [Ansible best practices](https://docs.ansible.com/ansible/latest/playbook_guide/index.html) - Role layout and idempotency patterns.

## Proof-of-concept prompts
- Build a minimum viable runbook for `iac-ansible` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `iac-ansible` before finalizing changes.
