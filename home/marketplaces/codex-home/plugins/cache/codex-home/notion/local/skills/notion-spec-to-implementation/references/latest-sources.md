---
title: notion-spec-to-implementation reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- notion-spec-to-implementation
- references
- latest-sources-md
- latest-sources
- user
- chatgpt
updated: '2026-02-20'
---
# notion-spec-to-implementation reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

## SKILL.md coverage checklist
- Use this skill when
- Quick start
- Workflow
- 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
- 1) Locate and read the spec
- 2) Choose plan depth
- 3) Create tasks
- 4) Link artifacts
- 5) Track progress
- Agent orchestration
- Validation and testing
- Outputs
- References and examples

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-spec-to-implementation/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-spec-to-implementation/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-spec-to-implementation/reference/` (previous notes retained by this skill)

## External references
- [Notion API intro](https://developers.notion.com/reference/intro) - Notion integration behavior and limits.
- [Notion block API](https://developers.notion.com/reference/block) - Spec decomposition and structured task mapping.

## Proof-of-concept prompts
- Build a minimum viable runbook for `notion-spec-to-implementation` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `notion-spec-to-implementation` before finalizing changes.

