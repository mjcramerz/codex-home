---
name: pack-docs
description: Create or update pack documentation and workflows under $CODEX_HOME/docs/.
  Use when adding new guides, updating doc indexes, or aligning docs with prompts, templates,
  and skills.
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
  default-prompt: Act as the "PACK-Docs" specialist for "Maintain pack documentation and workflows".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# PACK-Docs

## Use this skill when
- adding or editing documentation in `$CODEX_HOME/docs/`
- updating `$CODEX_HOME/docs/OVERVIEW.md` or domain overviews
- aligning docs with prompts, skills, and templates

## Inputs
- target doc paths and user-visible behavior that must stay stable
- required cross-links (prompts, templates, snippets, skills, index entrypoints)
- whether routing/index artifacts also need regeneration

## Scope and boundaries
- Edit source docs, not generated mirrors.
- Keep generated `BEGIN/END` blocks untouched unless generator tooling is run.
- Preserve existing semantics while improving clarity and discoverability.
- Use repo-relative or runtime-relative paths in prose; never hardcode workstation-specific repository paths.

## Workflow
1) Update or add docs in `$CODEX_HOME/docs/` (keep overview/README accurate).
2) Ensure cross-links to prompts, templates, skills, and snippets are correct.
3) Update `$CODEX_HOME/index/pack/docs.md` related links as needed.
4) When docs touch shell guidance, route through `$CODEX_HOME/docs/style/shell-runtime.md` and point shell-specific details at the matching language guide.

## Agent orchestration
- Delegate read-only doc/link discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Validate links and referenced paths for every touched doc.

## Outputs
- Reviewable doc diffs with updated links and routing references.
- Verification notes for index/pack checks that were run.
- Follow-up list when additional regeneration or docs sync is still needed.

## References
- `$CODEX_HOME/docs/OVERVIEW.md`
- `$CODEX_HOME/docs/workflows/overview.md`
- `$CODEX_HOME/index/pack/docs.md`
- `$CODEX_HOME/index/manifest.yml`
