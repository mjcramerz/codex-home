---
name: agent-orchestration
description: Decompose multi-agent coding work into owned slices, reconcile findings, and manage validation handoff without duplicating effort. Use when tasks need parallel explorers, workers, or staged integration.
metadata:
  version: '1.0'
  short-description: Plan and reconcile multi-agent coding work
  tags:
  - agents
  - delegation
  - planning
  - coordination
interface:
  display-name: AGENT-Orchestration
  short-description: Plan and reconcile multi-agent coding work
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#2563EB'
  default-prompt: Act as the "AGENT-Orchestration" specialist for "Plan and reconcile multi-agent coding work". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Split work by ownership and critical path, not by arbitrary file count.
2) Delegate only bounded scouting or isolated implementation slices with clean boundaries.
3) Reconcile results into one final owner path before validation and handoff.

## Agent orchestration
- Confirm ownership, validation scope, and whether another skill or plugin should be combined before editing.
- Delegate only bounded scouting or independent verification work.

## Validation and testing
- Run the narrowest syntax, parser, or unit checks that prove the change.
- Explicitly call out skipped checks and why they remain out of scope.

## Outputs
- Minimal, reviewable edits aligned to the skill contract.
- Concrete validation commands and residual risks.

## References
- [Model Context Protocol](https://modelcontextprotocol.io/introduction)
- [OpenAI tools guide](https://platform.openai.com/docs/guides/tools)
