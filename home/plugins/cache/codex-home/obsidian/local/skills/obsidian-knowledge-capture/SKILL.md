---
name: obsidian-knowledge-capture
description: Capture conversations and decisions into structured Obsidian notes. Use when
  converting chats, specs, or notes into reusable knowledge artifacts inside an Obsidian vault.
metadata:
  version: '1.0'
  short-description: Obsidian knowledge capture workflows
  tags:
  - obsidian
  - knowledge
  - capture
  - notes
interface:
  display-name: OBSIDIAN-Knowledge Capture
  short-description: Obsidian knowledge capture workflows
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC6332'
  default-prompt: Act as the "OBSIDIAN-Knowledge Capture" specialist for "Obsidian knowledge
    capture workflows". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

# OBSIDIAN-Knowledge Capture

## Overview

Turn raw notes into structured Obsidian documents with templates, tags, and links.

## Workflow
1) Clarify the artifact type (decision, how-to, FAQ, runbook).
2) Use `references/FORMS.md` to gather missing inputs.
3) Choose a template from `assets/`.
4) Create the note with consistent frontmatter and links.
5) Add backlinks to relevant indexes.

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
- **Form filling**: See [FORMS.md](references/FORMS.md).
- **API reference**: See [REFERENCE.md](references/REFERENCE.md).
- **Examples**: See [EXAMPLES.md](references/EXAMPLES.md).

## Resources
- `assets/decision-template.md`
- `assets/howto-template.md`
