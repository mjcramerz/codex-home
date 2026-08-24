---
title: notion-meeting-intelligence reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- notion-meeting-intelligence
- references
- latest-sources-md
- latest-sources
- user
- chatgpt
updated: '2026-02-20'
---
# notion-meeting-intelligence reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

## SKILL.md coverage checklist
- Use this skill when
- Quick start
- Workflow
- 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
- 1) Gather inputs
- 2) Choose format
- 3) Build the agenda/pre-read
- 4) Enrich with research
- 5) Finalize and share
- Agent orchestration
- Validation and testing
- Outputs
- References and examples

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-meeting-intelligence/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-meeting-intelligence/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-meeting-intelligence/reference/` (previous notes retained by this skill)

## External references
- [Notion API intro](https://developers.notion.com/reference/intro) - Notion integration behavior and limits.
- [Notion database query API](https://developers.notion.com/reference/post-database-query) - Meeting note retrieval and synthesis workflow inputs.

## Proof-of-concept prompts
- Build a minimum viable runbook for `notion-meeting-intelligence` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `notion-meeting-intelligence` before finalizing changes.

