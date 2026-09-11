---
name: pack-rules
description: Use this skill to create or update execpolicy rules and guidance under
  $CODEX_HOME/rules/. Use when adding new rule files, adjusting ordering, or updating
  execpolicy documentation and index links.
metadata:
  version: '1.0'
  short-description: Maintain execpolicy rules and guidance
  tags:
  - rules
  - execpolicy
  - security
  - pack
interface:
  display-name: PACK-Rules
  short-description: Maintain execpolicy rules and guidance
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7F32CC'
  default-prompt: Act as the "PACK-Rules" specialist for "Maintain execpolicy rules
    and guidance". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Pack Rules

## Workflow

1. Identify the canonical execution-policy rules, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write execution-policy rules directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/rules/`
- `$CODEX_HOME/rules/OVERVIEW.md`
- `$CODEX_HOME/index/pack/rules.md`
- `$CODEX_HOME/index/core/execpolicy.md`
- `$CODEX_HOME/rules/00-core.rules`
- `$CODEX_HOME/rules/10-vcs.rules`
- `$CODEX_HOME/rules/12-scripting.rules`
- `$CODEX_HOME/rules/20-network.rules`
- `$CODEX_HOME/rules/25-packages.rules`
- `$CODEX_HOME/rules/30-system.rules`
- `$CODEX_HOME/rules/35-crypto.rules`
- `$CODEX_HOME/rules/40-infra.rules`
- `$CODEX_HOME/rules/90-forbidden.rules`
- `$CODEX_HOME/docs/workflows/execpolicy.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
