---
title: pack-rules reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-rules
- references
- latest-sources-md
- latest-sources
- admin
updated: '2026-02-25'
---
# pack-rules reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Create or update execpolicy rules and guidance under $CODEX_HOME/rules/. Use when adding new rule files, adjusting ordering, or updating execpolicy documentation and index links.

## SKILL.md coverage checklist
- Use this skill when
- Inputs
- Scope and boundaries
- Workflow
- Rule safety checklist
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/pack-rules/SKILL.md`
- `$CODEX_SKILLS/pack-rules/agents/openai.yaml`

## External references
- [YAML 1.2 specification](https://yaml.org/spec/1.2.2/) - Manifest syntax and deterministic formatting rules.
- [OPA policy language docs](https://www.openpolicyagent.org/docs/latest/policy-language/) - Rule authoring patterns and guardrails.
- [Rego style guide](https://www.openpolicyagent.org/docs/latest/style-guide/) - Policy readability and maintainability conventions.

## Proof-of-concept prompts
- Build a minimum viable runbook for `pack-rules` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `pack-rules` before finalizing changes.
