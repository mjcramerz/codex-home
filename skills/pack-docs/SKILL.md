---
name: pack-docs
description: Use this skill to create or update pack documentation and workflows under
  $CODEX_HOME/docs/. Use when adding new guides, updating doc indexes, or aligning
  docs with prompts, templates, and skills.
metadata:
  version: '1.0'
  short-description: Maintain pack documentation and workflows
  tags:
  - docs
  - documentation
  - workflows
  - pack
interface:
  display-name: PACK-Docs
  short-description: Maintain pack documentation and workflows
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC327C'
  default-prompt: Act as the "PACK-Docs" specialist for "Maintain pack documentation
    and workflows". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Pack Docs

## Workflow

1. Identify the canonical docs and workflows, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write docs and workflows directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/docs/`
- `$CODEX_HOME/docs/OVERVIEW.md`
- `$CODEX_HOME/index/pack/docs.md`
- `$CODEX_HOME/docs/style/shell-runtime.md`
- `$CODEX_HOME/docs/workflows/overview.md`
- `$CODEX_HOME/index/manifest.yml`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
