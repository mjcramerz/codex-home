---
name: pack-templates
description: Create or update pack templates under $CODEX_HOME/templates/. Use when adding
  scaffolds, adjusting template READMEs, or wiring template references into docs and indexes.
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
  default-prompt: Act as the "PACK-Templates" specialist for "Maintain pack templates and
    scaffolds". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

# PACK-Templates

## Use this skill when
- adding or updating template scaffolds in `$CODEX_HOME/templates/`
- updating template README files
- aligning templates with prompts and docs

## Inputs
- target template path(s) and expected consumer workflow
- compatibility constraints (existing variables/placeholders and command names)
- docs/index entries that must point to the template

## Scope and boundaries
- Keep templates reusable and deterministic; avoid embedding environment-specific secrets.
- Keep README instructions concise and copy/paste-safe.
- Preserve existing template interfaces unless explicitly asked to change them.

## Workflow
1) Create/update template files under `$CODEX_HOME/templates/` with clear README usage notes.
2) Update `$CODEX_HOME/templates/OVERVIEW.md` to list new templates and entrypoints.
3) Ensure docs reference the template where relevant.
4) For shell templates, keep Bash templates wired to `$CODEX_HOME/UNIX.md` and POSIX sh templates wired to `$CODEX_HOME/docs/style/sh.md`.
5) Update `$CODEX_HOME/index/pack/templates.md` related links if needed.

## Agent orchestration
- Delegate read-only template inventory/link checks only.
- Keep one owner for template edits and final verification output.

## Validation and testing
- Validate template placeholders/variables and README command examples.
- Recheck docs/index links for every added or renamed template entry.

## Outputs
- Template diffs plus README updates that explain usage and constraints.
- Linked docs/index updates for discoverability.
- Verification evidence from pack checks.

## References
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/docs/templates/overview.md`
- `$CODEX_HOME/docs/templates/using-templates.md`
- `$CODEX_HOME/index/pack/templates.md`
