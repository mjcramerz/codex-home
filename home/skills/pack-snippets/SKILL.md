---
name: pack-snippets
description: Use this skill to create or update hardened snippets under $CODEX_HOME/snippets/.
  Use when adding reusable patterns, updating snippet catalogs, or wiring snippets
  into docs and indexes.
metadata:
  version: '1.0'
  short-description: Maintain pack snippets and patterns
  tags:
  - snippets
  - patterns
  - pack
interface:
  display-name: PACK-Snippets
  short-description: Maintain pack snippets and patterns
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC3298'
  default-prompt: Act as the "PACK-Snippets" specialist for "Maintain pack snippets
    and patterns". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Pack Snippets

## Workflow

1. Identify the canonical copyable code snippets, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write copyable code snippets directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/snippets/`
- `$CODEX_HOME/snippets/OVERVIEW.md`
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/index/pack/snippets.md`
- `$CODEX_HOME/docs/OVERVIEW.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
