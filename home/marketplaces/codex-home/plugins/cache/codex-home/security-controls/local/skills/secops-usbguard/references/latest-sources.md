---
title: secops-usbguard reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- secops-usbguard
- references
- latest-sources-md
- latest-sources
- user
- security
updated: '2026-02-20'
---

# secops-usbguard reference bundle

Consult this reference when secops-usbguard reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Configure USBGuard rules and policies.

## SKILL.md coverage checklist

- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors

- `$CODEX_HOME/plugins/security-controls/skills/secops-usbguard/SKILL.md`
- `$CODEX_HOME/plugins/security-controls/skills/secops-usbguard/agents/openai.yaml`

## External references

- [USBGuard docs](https://usbguard.github.io/) - Policy and device allowlist guidance.

## Proof-of-concept prompts

- Build a minimum viable runbook for `secops-usbguard` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `secops-usbguard` before finalizing changes.
