---
title: pack-index reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-index
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# pack-index reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Maintain and update the pack routing index, including $CODEX_HOME/index/manifest.yml, $CODEX_HOME/index/ entrypoints, and generated $CODEX_HOME/INDEX.md. Use when adding/removing entrypoints, updating related links, or regenerating index artifacts.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/pack-index/SKILL.md`
- `$CODEX_SKILLS/pack-index/agents/openai.yaml`

## External references
- [YAML 1.2 specification](https://yaml.org/spec/1.2.2/) - Manifest syntax and deterministic formatting rules.
- [JSON Schema draft 2020-12](https://json-schema.org/draft/2020-12) - Schema versioning and validation conventions.

## Proof-of-concept prompts
- Build a minimum viable runbook for `pack-index` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `pack-index` before finalizing changes.

