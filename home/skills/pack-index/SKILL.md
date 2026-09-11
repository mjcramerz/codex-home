---
name: pack-index
description: Use this skill to maintain and update the pack routing index, including
  $CODEX_HOME/index/manifest.yml, $CODEX_HOME/index/ entrypoints, and generated $CODEX_HOME/INDEX.md.
  Use when adding/removing entrypoints, updating related links, or regenerating index
  artifacts.
metadata:
  version: '1.0'
  short-description: Maintain pack index and routing
  tags:
  - index
  - routing
  - manifest
  - pack
interface:
  display-name: PACK-Index
  short-description: Maintain pack index and routing
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7032CC'
  default-prompt: Act as the "PACK-Index" specialist for "Maintain pack index and
    routing". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

# Pack Index

## Workflow

1. Identify the canonical routing indexes and manifests, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write routing indexes and manifests directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/index/manifest.yml`
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/index/`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
