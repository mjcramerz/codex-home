---
name: pack-snippets
description: Create or update hardened snippets under $CODEX_HOME/snippets/. Use when
  adding reusable patterns, updating snippet catalogs, or wiring snippets into docs and indexes.
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
  default-prompt: Act as the "PACK-Snippets" specialist for "Maintain pack snippets and patterns".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# PACK-Snippets

## Use this skill when
- adding or editing reusable snippets in `$CODEX_HOME/snippets/`
- updating `$CODEX_HOME/snippets/OVERVIEW.md`
- referencing snippets from docs or prompts

## Inputs
- target snippet files and language/runtime context
- intended usage boundaries (safe defaults, non-goals, portability needs)
- docs/prompts that should link to the snippet

## Scope and boundaries
- Prefer small, composable snippets with clear guardrails.
- Keep snippet examples deterministic and security-aware.
- Avoid duplicating the same snippet logic across multiple files when one canonical path is enough.

## Workflow
1) Add or update snippet files and organize by domain/language.
2) Update `$CODEX_HOME/snippets/OVERVIEW.md` with new entries and usage notes.
3) Ensure docs and prompts reference the snippet where useful.
4) For shell snippets, keep Bash snippets wired to `$CODEX_HOME/UNIX.md` and POSIX sh snippets wired to `$CODEX_HOME/docs/style/sh.md`.
5) Update `$CODEX_HOME/index/pack/snippets.md` related links if needed.

## Agent orchestration
- Delegate read-only snippet inventory/link checks only.
- Keep one owner for snippet edits and final verification output.

## Validation and testing
- Validate snippet examples for syntax and deterministic behavior in their target runtime.
- Recheck overview/docs/prompt links for every added or moved snippet.

## Outputs
- Reviewable snippet and catalog diffs.
- Updated link map for docs/prompts that consume the snippet.
- Verification evidence from pack checks.

## References
- `$CODEX_HOME/snippets/OVERVIEW.md`
- `$CODEX_HOME/index/pack/snippets.md`
- `$CODEX_HOME/docs/OVERVIEW.md`
