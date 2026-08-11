---
name: test-strategy
description: Choose narrow, risk-based verification plans and turn code changes into targeted tests, sanity checks, and regression coverage. Use when the task is ambiguous, high-impact, or needs a concrete validation plan before editing.
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
  default-prompt: Act as the "TEST-Strategy" specialist for "Map code changes to focused tests and regression checks". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Identify the changed behavior and the cheapest command that proves it.
2) Separate syntax, unit, integration, and end-to-end validation instead of blending them.
3) Call out skipped checks and the exact reason they remain out of scope.

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
- [pytest docs](https://docs.pytest.org/)
- [unittest](https://docs.python.org/3/library/unittest.html)
- [cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
