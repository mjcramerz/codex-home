---
title: Workflow patterns for skills
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-skills
- references
- workflows-md
- workflows
- user
- default
updated: '2026-02-20'
---
# Workflow patterns for skills
Guidance for structuring multi-step skill workflows with clear sequencing and decision points.

## Default flow (apply unless overridden)
1) **Clarify intent** — restate the goal and constraints.
2) **Discover context** — locate entrypoints, configs, tests, and conventions.
3) **Select path** — prefer workflows/plans/templates/snippets before skills; use prompts as macros after plan selection.
4) **Plan** — create/update a plan before coding when triggers in `$CODEX_HOME/AGENTS.md` apply.
5) **Implement** — minimal diffs, deterministic steps.
6) **Validate** — run the narrowest relevant checks.
7) **Harden** — handle error paths, limits, auth boundaries.
8) **Report** — summary, tests, risks, next steps.

## Decision points
- **Missing inputs**: ask 1–2 focused questions; otherwise proceed with stated assumptions.
- **Risky changes**: require explicit confirmation (filesystem ops, prod data, destructive actions).
- **Multiple paths**: pick the lowest-risk option and explain trade-offs.

## Guardrails
- Preserve behavior unless explicitly requested.
- Treat inputs as hostile; validate size/shape/timeouts.
- No new dependencies unless clearly justified.
- Prefer workflows/plans/templates before skills.
- Related lists may place prompts first for discoverability; routing order still applies.
- Place skills last in related lists.

## Checklist template
- [ ] Restate goal, constraints, and non-goals
- [ ] Identify entrypoints and conventions
- [ ] Choose prompt/workflow/template/skill path
- [ ] Draft/update plan (if any plan-before-coding trigger applies; see `$CODEX_HOME/AGENTS.md`)
- [ ] Implement minimal change
- [ ] Validate with tests/linters
- [ ] Summarize outputs and risks
