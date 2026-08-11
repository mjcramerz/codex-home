---
title: secops-auditd reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- secops-auditd
- references
- latest-sources-md
- latest-sources
- user
- security
updated: '2026-02-20'
---
# secops-auditd reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Configure auditd rules and logging safely.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/security-controls/local/skills/secops-auditd/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/security-controls/local/skills/secops-auditd/agents/openai.yaml`

## External references
- [auditd man page](https://man7.org/linux/man-pages/man8/auditd.8.html) - Audit daemon behavior and lifecycle controls.

## Proof-of-concept prompts
- Build a minimum viable runbook for `secops-auditd` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `secops-auditd` before finalizing changes.
