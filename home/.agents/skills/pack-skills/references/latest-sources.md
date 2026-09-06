---
title: pack-skills reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-skills
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# pack-skills reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.

## SKILL.md coverage checklist
- Use this skill when
- About Skills
- What Skills Provide
- Core Principles
- Concise is Key
- Set Appropriate Degrees of Freedom
- Anatomy of a Skill
- Agent orchestration
- Validation and testing
- Outputs
- References (this directory)
- Progressive Disclosure Design Principle
- Quick start
- Advanced features
- Creating documents
- Editing documents
- Skill Creation Process
- Skill Naming

## Local implementation anchors
- `$CODEX_SKILLS/pack-skills/SKILL.md`
- `$CODEX_SKILLS/pack-skills/agents/openai.yaml`

## External references
- [YAML 1.2 specification](https://yaml.org/spec/1.2.2/) - Manifest syntax and deterministic formatting rules.
- [OpenAI prompt engineering guide](https://developers.openai.com/docs/guides/prompt-engineering) - Skill prompt composition and instruction quality.

## Proof-of-concept prompts
- Build a minimum viable runbook for `pack-skills` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `pack-skills` before finalizing changes.
