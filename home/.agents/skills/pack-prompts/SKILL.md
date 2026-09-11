---
name: pack-prompts
description: Use this skill to create or update runtime prompt assets under $CODEX_HOME/.prompt/.
  Use when refining prompt contracts, adding operator-local prompt files, or improving
  prompt-maintenance assets.
metadata:
  version: '1.0'
  short-description: Maintain pack prompts and prompt-maintenance assets
  tags:
  - pack-prompts
  - prompts
  - pack
interface:
  display-name: PACK-Prompts
  short-description: Maintain pack prompts and prompt-maintenance assets
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC6A32'
  default-prompt: Act as the "PACK-Prompts" specialist for "Maintain pack prompts
    and prompt-maintenance assets". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Pack Prompts

## Workflow

1. Identify the canonical prompt and instruction assets, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write prompt and instruction assets directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/.prompt/`
- `$CODEX_HOME/docs/create-prompts.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
