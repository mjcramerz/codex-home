---
name: pack-templates
description: Use this skill to create or update pack templates under $CODEX_HOME/templates/.
  Use when adding scaffolds, adjusting template READMEs, or wiring template references
  into docs and indexes.
metadata:
  version: '1.0'
  short-description: Maintain pack templates and scaffolds
  tags:
  - templates
  - scaffolding
  - pack
interface:
  display-name: PACK-Templates
  short-description: Maintain pack templates and scaffolds
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#AF32CC'
  default-prompt: Act as the "PACK-Templates" specialist for "Maintain pack templates
    and scaffolds". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Pack Templates

## Workflow

1. Identify the canonical project and file templates, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write project and file templates directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/templates/`
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/index/pack/templates.md`
- `$CODEX_HOME/docs/templates/overview.md`
- `$CODEX_HOME/docs/templates/using-templates.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
