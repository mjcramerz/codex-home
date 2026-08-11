---
name: data-json
description: Edit and validate JSON, YAML, and TOML with schema-aware, minimal-diff changes and deterministic formatting decisions. Use when the task centers on structured config, manifests, metadata catalogs, or payload transformation.
metadata:
  version: '1.0'
  short-description: Edit JSON, YAML, and TOML safely with schema awareness
  tags:
  - json
  - yaml
  - toml
  - config
  - schema
interface:
  display-name: DATA-Config Formats
  short-description: Edit JSON, YAML, and TOML safely with schema awareness
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#F59E0B'
  default-prompt: Act as the "DATA-Config Formats" specialist for "Edit JSON, YAML, and TOML safely with schema awareness". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Parse the current payload before proposing changes.
2) Preserve comments, ordering intent, and user-managed keys when formats allow it.
3) Validate the final payload with the narrowest parser or schema check available.

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
- [TOML](https://toml.io/en/)
