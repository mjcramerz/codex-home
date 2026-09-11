---
name: workflow-plans
description: Use this skill to generate concise execution plans for multi-step or
  ambiguous engineering tasks with milestones, risks, and validation checkpoints.
  Use when the user asks for a plan, roadmap, or phased implementation strategy.
metadata:
  version: '1.0'
  short-description: Generate a plan for a complex task
  tags:
  - plan
  - guide
  - onboarding
interface:
  display-name: WORKFLOW-Plans
  short-description: Generate a plan for a complex task
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CCC132'
  default-prompt: Act as the "WORKFLOW-Plans" specialist for "Generate a plan for
    a complex task". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Workflow Plans

## Workflow

1. Extract the outcome, owned paths, constraints, evidence and explicit non-goals from the active request.

2. Create ordered steps with concrete outputs, dependencies and completion criteria. Keep immediate work executable and avoid generic checklist padding.

3. Attach security, rollback and validation steps only where relevant to the actual change. Do not schedule unrequested deployment or create prohibited files.

4. Update status from observed work, record blockers precisely and finish with completed outputs and remaining risks.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/plans`
- `$CODEX_HOME/docs/`
- `$CODEX_HOME/plans/OVERVIEW.md`
- `$CODEX_HOME/docs/prompt-writing.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
