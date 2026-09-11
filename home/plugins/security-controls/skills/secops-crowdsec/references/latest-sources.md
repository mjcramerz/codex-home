---
title: secops-crowdsec reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- secops-crowdsec
- references
- latest-sources-md
- latest-sources
- user
- security
updated: '2026-02-20'
---

# secops-crowdsec reference bundle

Consult this reference when secops-crowdsec reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Configure CrowdSec collections, log sources, and bouncers safely.

## SKILL.md coverage checklist

- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors

- `$CODEX_HOME/plugins/security-controls/skills/secops-crowdsec/SKILL.md`
- `$CODEX_HOME/plugins/security-controls/skills/secops-crowdsec/agents/openai.yaml`

## External references

- [CrowdSec docs](https://docs.crowdsec.net/docs/next/getting_started/intro/) - CrowdSec engine and parser setup.
- [CrowdSec parser docs](https://docs.crowdsec.net/docs/next/parsers/format/) - Parser tuning and detection flow.

## Proof-of-concept prompts

- Build a minimum viable runbook for `secops-crowdsec` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `secops-crowdsec` before finalizing changes.
