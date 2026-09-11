---
title: secops-aide reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- secops-aide
- references
- latest-sources-md
- latest-sources
- user
- security
updated: '2026-02-20'
---

# secops-aide reference bundle

Consult this reference when secops-aide reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Configure AIDE file integrity monitoring.

## SKILL.md coverage checklist

- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors

- `$CODEX_HOME/plugins/security-controls/skills/secops-aide/SKILL.md`
- `$CODEX_HOME/plugins/security-controls/skills/secops-aide/agents/openai.yaml`

## External references

- [AIDE man page](https://manpages.debian.org/stable/aide/aide.1.en.html) - AIDE rule and check semantics.

## Proof-of-concept prompts

- Build a minimum viable runbook for `secops-aide` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `secops-aide` before finalizing changes.
