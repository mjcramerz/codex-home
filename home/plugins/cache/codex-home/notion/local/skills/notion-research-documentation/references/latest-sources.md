---
title: notion-research-documentation reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- notion-research-documentation
- references
- latest-sources-md
- latest-sources
- user
- chatgpt
updated: '2026-02-20'
---
# notion-research-documentation reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

## SKILL.md coverage checklist
- Use this skill when
- Quick start
- Workflow
- 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
- 1) Gather sources
- 2) Select the format
- 3) Synthesize
- 4) Create the doc
- 5) Finalize & handoff
- Agent orchestration
- Validation and testing
- Outputs
- References and examples

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-research-documentation/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-research-documentation/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/notion/local/skills/notion-research-documentation/reference/` (previous notes retained by this skill)

## External references
- [Notion API intro](https://developers.notion.com/reference/intro) - Notion integration behavior and limits.
- [Notion search API](https://developers.notion.com/reference/post-search) - Cross-source research retrieval patterns.

## Proof-of-concept prompts
- Build a minimum viable runbook for `notion-research-documentation` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `notion-research-documentation` before finalizing changes.

