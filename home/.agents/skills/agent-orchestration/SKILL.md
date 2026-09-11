---
name: agent-orchestration
description: Use this skill to decompose multi-agent coding work into owned slices,
  reconcile findings, and manage validation handoff without duplicating effort. Use
  when tasks need parallel explorers, workers, or staged integration.
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
  default-prompt: Act as the "AGENT-Orchestration" specialist for "Plan and reconcile
    multi-agent coding work". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Agent Orchestration

## Workflow

1. Decompose the objective into independent slices with explicit dependencies and a single integration owner. Keep the next blocking step local.

2. Assign each child an objective, owned paths, allowed actions, output contract and stop condition. Use only currently available agent tools.

3. Do not allow concurrent edits to shared files. Reuse an existing child context for follow-up and reconcile claims against inspected evidence.

4. Integrate the authorized changes, run focused checks and close or stop child work once its accepted output is consumed.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
