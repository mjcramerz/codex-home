---
name: config-audit
description: Audit config fragments, merge order, placeholder materialization, and policy drift with concrete risk calls and validation follow-up. Use when the user asks to review config layout, runtime overlays, or managed configuration contracts.
metadata:
  version: '1.0'
  short-description: Audit config merge order, placeholders, and policy drift
  tags:
  - audit
  - config
  - policy
  - drift
interface:
  display-name: AUDIT-Config
  short-description: Audit config merge order, placeholders, and policy drift
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#0F766E'
  default-prompt: Act as the "AUDIT-Config" specialist for "Audit config merge order, placeholders, and policy drift". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Trace config sources, merge order, and placeholder expansion before proposing fixes.
2) Separate schema violations from product-choice disagreements.
3) Map each finding to a concrete command or file proof point.

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
- [TOML](https://toml.io/en/)
