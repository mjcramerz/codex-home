---
name: obsidian-spec-to-implementation
description: Convert specs into implementation plans and task notes in Obsidian. Use when
  turning PRDs or feature specs into plans, checklists, and linked tasks in an Obsidian vault.
metadata:
  version: '1.0'
  short-description: Obsidian spec-to-implementation workflow
  tags:
  - obsidian
  - specs
  - planning
  - tasks
interface:
  display-name: OBSIDIAN-Spec to Implementation
  short-description: Obsidian spec-to-implementation workflow
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC7A'
  default-prompt: Act as the "OBSIDIAN-Spec to Implementation" specialist for "Obsidian spec-to-implementation
    workflow". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

# OBSIDIAN-Spec to Implementation

## Overview

Translate specs into structured plans and task lists inside Obsidian.

## Workflow
1) Parse the spec and extract requirements.
2) Draft an implementation plan using `assets/spec-implementation-template.md`.
3) Create task lists and link related notes.
4) Track progress with consistent status fields.

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
- `assets/spec-implementation-template.md`
