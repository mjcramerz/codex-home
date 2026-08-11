---
title: pack-docs reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-docs
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# pack-docs reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Create or update pack documentation and workflows under $CODEX_HOME/docs/. Use when adding new guides, updating doc indexes, or aligning docs with prompts, templates, and skills.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/pack-docs/SKILL.md`
- `$CODEX_SKILLS/pack-docs/agents/openai.yaml`

## External references
- [YAML 1.2 specification](https://yaml.org/spec/1.2.2/) - Manifest syntax and deterministic formatting rules.
- [Markdown style guide](https://www.markdownguide.org/basic-syntax/) - Documentation formatting baseline.

## Proof-of-concept prompts
- Build a minimum viable runbook for `pack-docs` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `pack-docs` before finalizing changes.

