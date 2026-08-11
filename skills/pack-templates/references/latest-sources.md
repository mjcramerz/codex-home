---
title: pack-templates reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-templates
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# pack-templates reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Create or update pack templates under $CODEX_HOME/templates/. Use when adding scaffolds, adjusting template READMEs, or wiring template references into docs and indexes.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/pack-templates/SKILL.md`
- `$CODEX_SKILLS/pack-templates/agents/openai.yaml`

## External references
- [YAML 1.2 specification](https://yaml.org/spec/1.2.2/) - Manifest syntax and deterministic formatting rules.
- [Jinja template docs](https://jinja.palletsprojects.com/en/stable/templates/) - Template rendering and reuse patterns.

## Proof-of-concept prompts
- Build a minimum viable runbook for `pack-templates` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `pack-templates` before finalizing changes.

