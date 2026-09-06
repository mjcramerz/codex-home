---
name: obsidian-research-documentation
description: Research across sources and synthesize into structured Obsidian documentation.
  Use when producing briefs, comparisons, or research reports in an Obsidian vault.
metadata:
  version: '1.0'
  short-description: Obsidian research documentation workflow
  tags:
  - obsidian
  - research
  - documentation
  - reports
interface:
  display-name: OBSIDIAN-Research Docs
  short-description: Obsidian research documentation workflow
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC32A0'
  default-prompt: Act as the "OBSIDIAN-Research Docs" specialist for "Obsidian research documentation
    workflow". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

# OBSIDIAN-Research Docs

## Overview

Synthesize research into clear Obsidian notes with sources and structured sections.

## Workflow
1) Define scope and target audience.
2) Capture sources and key findings.
3) Draft a structured report in Obsidian.
4) Add citations and related links.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs

- Actionable steps or artifacts aligned to the skill.
- References to relevant files, commands, or templates.

## References
- **API reference**: See [REFERENCE.md](references/REFERENCE.md) for report structure.
- **Examples**: See [EXAMPLES.md](references/EXAMPLES.md).
