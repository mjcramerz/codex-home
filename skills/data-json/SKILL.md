---
name: data-json
description: Use this skill to edit and validate JSON, YAML, and TOML with schema-aware,
  minimal-diff changes and deterministic formatting decisions. Use when the task centers
  on structured config, manifests, metadata catalogs, or payload transformation.
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
  default-prompt: Act as the "DATA-Config Formats" specialist for "Edit JSON, YAML,
    and TOML safely with schema awareness". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete
    actions, evidence, and residual risks.
---

# Data Json

## Workflow

1. Identify the serialization format, schema version and canonical source. Preserve ordering/comments where the format and chosen parser support them.

2. Parse with JSON, TOML or safe YAML libraries rather than regex substitution. Validate types, duplicate keys and required fields before mutation.

3. Apply a minimal transformation and write atomically when replacing runtime state. Preserve template variables and do not serialize secrets into examples.

4. Reparse the output, verify relevant invariants and report format validation separately from consumer/runtime compatibility.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
