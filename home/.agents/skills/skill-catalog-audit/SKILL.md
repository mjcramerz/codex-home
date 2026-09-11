---
name: skill-catalog-audit
description: Use this skill to audit skill metadata, routing coverage, namespace structure,
  and plugin bundle assignments for drift or missing capability coverage. Use this
  skill when you need to review skill catalogs, plugin manifests, or routing quality.
metadata:
  version: '1.0'
  short-description: Audit skill metadata, routing coverage, and bundle mapping
  tags:
  - audit
  - skills
  - routing
  - metadata
interface:
  display-name: AUDIT-Skill Catalog
  short-description: Audit skill metadata, routing coverage, and bundle mapping
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#14B8A6'
  default-prompt: Act as the "AUDIT-Skill Catalog" specialist for "Audit skill metadata,
    routing coverage, and bundle mapping". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete
    actions, evidence, and residual risks.
---

# Skill Catalog Audit

## Workflow

1. Enumerate canonical skills, names, frontmatter triggers, plugin ownership and configured mirrors. Resolve names to real entrypoints.

2. Check routing against actual task coverage rather than generic descriptions. Keep IDs and interface metadata consistent across mirrors.

3. Validate referenced resources, tool dependencies and trust assumptions without invoking unrelated integrations.

4. Correct the smallest coherent set of entrypoints and mirrors; report missing capabilities instead of inventing installed tools.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
