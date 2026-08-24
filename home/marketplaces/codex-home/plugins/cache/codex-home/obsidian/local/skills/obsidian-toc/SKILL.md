---
name: obsidian-toc
description: Generate or update a table of contents for Obsidian Markdown notes. Use when
  a note needs a consistent TOC or when headings have changed.
metadata:
  version: '1.0'
  short-description: Obsidian table of contents automation
  tags:
  - obsidian
  - toc
  - markdown
  - automation
interface:
  display-name: OBSIDIAN-TOC
  short-description: Obsidian table of contents automation
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32C6CC'
  default-prompt: Act as the "OBSIDIAN-TOC" specialist for "Obsidian table of contents automation".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# OBSIDIAN-TOC

## Overview

Create or refresh a TOC for Markdown notes using the bundled script.

## Workflow
1) Identify the target Markdown file.
2) Run `python scripts/generate_toc.py` with appropriate depth.
3) Verify the TOC placement and links.

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
- **API reference**: See [REFERENCE.md](references/REFERENCE.md) for script options.
- **Examples**: See [EXAMPLES.md](references/EXAMPLES.md) for usage patterns.

## Resources
- `scripts/generate_toc.py` for deterministic TOC generation.
