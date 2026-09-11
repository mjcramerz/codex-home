---
name: test-strategy
description: Use this skill to choose narrow, risk-based verification plans and turn
  code changes into targeted tests, sanity checks, and regression coverage. Use when
  the task is ambiguous, high-impact, or needs a concrete validation plan before editing.
metadata:
  version: '1.0'
  short-description: Map code changes to focused tests and regression checks
  tags:
  - testing
  - qa
  - verification
  - regression
interface:
  display-name: TEST-Strategy
  short-description: Map code changes to focused tests and regression checks
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#10B981'
  default-prompt: Act as the "TEST-Strategy" specialist for "Map code changes to focused
    tests and regression checks". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Test Strategy

## Workflow

1. Map each changed behavior to a failure risk and a concrete observable outcome. Prefer existing tests and harnesses.

2. Choose the narrowest checks that distinguish the old failure from the corrected behavior. Include relevant malformed input, permissions and timeout boundaries.

3. Respect exclusions on new tests or general verification files. Use permitted ephemeral checks and report what they do not establish.

4. Broaden coverage only when dependencies or shared contracts justify it. Report commands, outcomes, skipped paths and live integration gaps.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
