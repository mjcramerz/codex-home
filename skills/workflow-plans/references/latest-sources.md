---
title: workflow-plans reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- workflow-plans
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# workflow-plans reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Generate a plan for how an agent should accomplish a complex coding task. Use when a user asks for a plan, and optionally when they want to save a plan under $CODEX_HOME/plans.

## SKILL.md coverage checklist
- Overview
- Core rules
- Workflow
- Plan discovery
- Plan creation workflow
- Plan update workflow
- Scripts (low-freedom helpers)
- Plan file format
- Implementation plan body template
- Requirements
- Scope
- Files and entry points
- Data model / API changes
- Action items
- Testing and validation
- Risks and edge cases
- Open questions
- Overview plan body template

## Local implementation anchors
- `$CODEX_SKILLS/workflow-plans/SKILL.md`
- `$CODEX_SKILLS/workflow-plans/agents/openai.yaml`

## External references
- [Project management lifecycle overview](https://www.atlassian.com/work-management/project-management/project-life-cycle) - Planning phases and execution checkpoints.
- [DORA metrics overview](https://cloud.google.com/architecture/devops/devops-tech-foundations) - Delivery metrics for workflow quality checks.

## Proof-of-concept prompts
- Build a minimum viable runbook for `workflow-plans` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `workflow-plans` before finalizing changes.
