---
title: notion-knowledge-capture reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- notion-knowledge-capture
- references
- latest-sources-md
- latest-sources
- user
- chatgpt
updated: '2026-02-20'
---
# notion-knowledge-capture reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

## SKILL.md coverage checklist
- Use this skill when
- Quick start
- Workflow
- 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
- 1) Define the capture
- 2) Locate destination
- 3) Extract and structure
- 4) Create/update in Notion
- 5) Link and surface
- Agent orchestration
- Validation and testing
- Outputs
- References and examples

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-knowledge-capture/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-knowledge-capture/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-knowledge-capture/reference/` (previous notes retained by this skill)

## External references
- [Notion API intro](https://developers.notion.com/reference/intro) - Notion integration behavior and limits.
- [Notion writing to API](https://developers.notion.com/reference/post-page) - Page creation and structured note capture APIs.

## Proof-of-concept prompts
- Build a minimum viable runbook for `notion-knowledge-capture` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `notion-knowledge-capture` before finalizing changes.

