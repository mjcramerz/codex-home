---
name: obsidian-meeting-intelligence
description: Prepare meeting materials and capture outcomes in Obsidian. Use when drafting
  agendas, pre-reads, decision logs, or follow-up tasks inside an Obsidian vault.
metadata:
  version: '1.0'
  short-description: Obsidian meeting prep and notes
  tags:
  - obsidian
  - meetings
  - agenda
  - notes
interface:
  display-name: OBSIDIAN-Meeting Intelligence
  short-description: Obsidian meeting prep and notes
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#6032CC'
  default-prompt: Act as the "OBSIDIAN-Meeting Intelligence" specialist for "Obsidian meeting
    prep and notes". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

# OBSIDIAN-Meeting Intelligence

## Overview

Produce consistent meeting notes, agendas, and follow-ups using templates and reference guidance.

## Workflow
1) Confirm meeting goal, attendees, and date/time.
2) Pull related context from the vault.
3) Use `assets/meeting-template.md` to draft the agenda and notes.
4) Record decisions and action items with clear owners and due dates.
5) Link the note to related project or decision notes.

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
- **API reference**: See [REFERENCE.md](references/REFERENCE.md) for meeting note structure.
- **Examples**: See [EXAMPLES.md](references/EXAMPLES.md) for sample notes.

## Resources
- `assets/meeting-template.md` for a consistent agenda/notes format.
