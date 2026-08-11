---
name: skill-catalog-audit
description: Audit skill metadata, routing coverage, namespace structure, and plugin bundle assignments for drift or missing capability coverage. Use when the user asks to review skill catalogs, plugin manifests, or routing quality.
metadata:
  version: '1.0'
  short-description: Audit skill metadata, routing coverage, and bundle mapping
  tags:
  - audit
  - skills
  - routing
  - metadata
interface:
  display-name: AUDIT-Skill Catalog
  short-description: Audit skill metadata, routing coverage, and bundle mapping
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#14B8A6'
  default-prompt: Act as the "AUDIT-Skill Catalog" specialist for "Audit skill metadata, routing coverage, and bundle mapping". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Check namespace coverage and required files before reviewing content quality.
2) Confirm every skill is discoverable through role/group or plugin bundle metadata.
3) Call out generator drift separately from actual content gaps.

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
- [YAML 1.2.2](https://yaml.org/spec/1.2.2/)
