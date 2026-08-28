---
title: iac-terraform reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- iac-terraform
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-20'
---
# iac-terraform reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Plan and review Terraform changes with safe defaults.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-terraform/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-terraform/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-terraform/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## External references
- [Terraform docs](https://developer.hashicorp.com/terraform/docs) - Infrastructure as code workflows and state handling.
- [Terraform style conventions](https://developer.hashicorp.com/terraform/language/style) - Readable and deterministic Terraform code.

## Proof-of-concept prompts
- Build a minimum viable runbook for `iac-terraform` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `iac-terraform` before finalizing changes.
