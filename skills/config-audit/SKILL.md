---
name: config-audit
description: Use this skill to audit config fragments, merge order, placeholder materialization,
  and policy drift with concrete risk calls and validation follow-up. Use this skill
  when you need to review config layout, runtime overlays, or managed configuration
  contracts.
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
  default-prompt: Act as the "AUDIT-Config" specialist for "Audit config merge order,
    placeholders, and policy drift". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Config Audit

## Workflow

1. Identify the loaded files, active profile, precedence order and environment substitutions. Trace each material value to its source.

2. Parse structured configuration with a real parser and compare only the release-specific definitions needed for the task. Preserve existing unrelated keys and comments.

3. Separate unsupported, deprecated, shadowed, unused and invalid settings. Do not silently delete custom keys or imply a syntactically valid file is accepted by every client.

4. Report the smallest corrective patch with exact source paths, precedence evidence and remaining runtime checks.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
