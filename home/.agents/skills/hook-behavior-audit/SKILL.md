---
name: hook-behavior-audit
description: Review startup, resume, and stop hooks for schema compliance, blocking behavior, repo-context quality, and validation-gate correctness. Use when the user asks to audit hook UX, guardrails, or lifecycle automation.
metadata:
  version: '1.0'
  short-description: Audit startup/resume/stop hooks and lifecycle guardrails
  tags:
  - audit
  - hooks
  - lifecycle
  - ux
interface:
  display-name: AUDIT-Hook Behavior
  short-description: Audit startup/resume/stop hooks and lifecycle guardrails
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#8B5CF6'
  default-prompt: Act as the "AUDIT-Hook Behavior" specialist for "Audit startup/resume/stop hooks and lifecycle guardrails". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Check hook input/output schema expectations before reading shell scripts.
2) Confirm which hooks add context, which warn, and which can block.
3) Verify that hook feedback stays specific, non-destructive, and evidence-based.

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
- [JSON Schema](https://json-schema.org/)
- [ShellCheck](https://www.shellcheck.net/)
