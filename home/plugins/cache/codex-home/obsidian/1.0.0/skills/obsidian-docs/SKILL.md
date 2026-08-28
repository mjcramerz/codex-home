---
name: obsidian-docs
description: Create, update, and structure Obsidian documentation vaults and notes. Use when
  organizing knowledge, standardizing frontmatter, building indexes, or applying templates
  inside an Obsidian vault.
metadata:
  version: '1.0'
  short-description: Obsidian documentation workflows
  tags:
  - obsidian
  - docs
  - knowledge
  - notes
interface:
  display-name: OBSIDIAN-Docs
  short-description: Obsidian documentation workflows
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#328ECC'
  default-prompt: Act as the "OBSIDIAN-Docs" specialist for "Obsidian documentation workflows".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# OBSIDIAN-Docs

## Overview

Establish consistent Obsidian documentation: frontmatter, naming conventions, folder structure, and reusable templates.

## Workflow
1) Confirm vault root and scope (notes to create or update).
2) Align on conventions using `references/REFERENCE.md`.
3) Collect requirements with `references/FORMS.md` when inputs are missing.
4) Apply templates from `assets/note-templates/`.
5) Ensure links/backlinks and indexes are updated.

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
- **Form filling**: See [FORMS.md](references/FORMS.md) for intake prompts.
- **API reference**: See [REFERENCE.md](references/REFERENCE.md) for frontmatter and structure rules.
- **Examples**: See [EXAMPLES.md](references/EXAMPLES.md) for sample notes.

## Resources
- `assets/note-templates/` for reusable note templates.
