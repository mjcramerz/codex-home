---
name: pack-skills
description: Use this skill to create or update Codex skills (SKILL.md, metadata,
  triggers, and bundled resources) with pack-compliant structure. Use this skill when
  you need to add a new skill, tune skill triggering, or improve skill assets/scripts/references.
metadata:
  version: '1.0'
  short-description: Create or update a skill
  tags:
  - skills
  - capability
  - knowledge
  - tools
interface:
  display-name: PACK-Skills
  short-description: Create or update a skill
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCB7'
  default-prompt: Act as the "PACK-Skills" specialist for "Create or update a skill".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

# Pack Skills

## Workflow

1. Identify the canonical skill entrypoints and resources, their consumers and generated/runtime mirrors. Inspect the current request before selecting files.

2. Write skill entrypoints and resources directly to the coding assistant with an explicit trigger, bounded procedure and stop condition. Preserve valid examples, placeholders and format contracts.

3. Resolve every changed local reference and tool dependency. Do not invent commands, imply tool availability from a manifest or inject full schemas as general context.

4. Keep related mirrors synchronized, reparse affected structured metadata and inspect rendered Markdown structure. Do not modify unrelated assets or create general tests outside scope.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
