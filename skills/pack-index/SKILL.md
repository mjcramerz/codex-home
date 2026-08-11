---
name: pack-index
description: Maintain and update the pack routing index, including $CODEX_HOME/index/manifest.yml,
  $CODEX_HOME/index/ entrypoints, and generated $CODEX_HOME/INDEX.md. Use when adding/removing
  entrypoints, updating related links, or regenerating index artifacts.
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
  default-prompt: Act as the "PACK-Index" specialist for "Maintain pack index and routing".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# PACK-Index

## Use this skill when
- adding or updating entrypoints in `$CODEX_HOME/index/manifest.yml`
- regenerating `$CODEX_HOME/INDEX.md` or domain routers
- fixing related link blocks in `$CODEX_HOME/index/` entrypoints

## Inputs
- target entrypoints and intended routing behavior
- canonical destination docs/paths for each entrypoint
- whether related lists/navigation blocks must be regenerated

## Scope and boundaries
- Treat `$CODEX_HOME/index/manifest.yml` as source of truth for routing generation.
- Do not hand-edit generated blocks that tooling will overwrite.
- Keep entrypoint links deterministic and one-hop where possible.
- Use runtime-relative paths or repo-relative paths; never hardcode workstation-specific checkout locations.

## Workflow
1) Update `$CODEX_HOME/index/manifest.yml` (entrypoints, canonical paths, related links, metadata).
2) Ensure every entrypoint file has a `<!-- BEGIN:related -->` block.
3) Spot-check key entrypoints for broken links.

## Agent orchestration
- Delegate read-only inventory checks (entrypoints, related-link drift) only.
- Keep one owner for manifest edits and generation commands.

## Validation and testing

## Outputs
- Minimal routing/index diffs with clear intent per entrypoint.
- Verification evidence from index generation/validation commands.
- Residual follow-ups when downstream docs still need linking updates.

## References
- `$CODEX_HOME/index/manifest.yml`
- `$CODEX_HOME/index/`
- `$CODEX_HOME/INDEX.md`
