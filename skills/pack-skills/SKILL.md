---
name: pack-skills
description: Create or update Codex skills (SKILL.md, metadata, triggers, and bundled resources)
  with pack-compliant structure. Use when the user asks to add a new skill, tune skill triggering,
  or improve skill assets/scripts/references.
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
  default-prompt: Act as the "PACK-Skills" specialist for "Create or update a skill". Deliver
    focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# PACK-Skills

## Use this skill when
- creating a new Codex skill or improving an existing one
- hardening skill routing, instructions, assets, and metadata quality
- aligning skill structure with current pack standards and verification gates

## Inputs
- target skill path (`$CODEX_SKILLS/<namespace>/<skill-name>/`) and whether it is new or existing
- expected trigger intent (what requests should activate the skill)
- required bundled resources (`scripts/`, `references/`, `assets/`)
- validation scope (single-skill checks or pack/catalog regeneration)

## Scope and boundaries
- Preserve trigger intent unless the user explicitly requests trigger changes.
- Keep SKILL bodies concise and procedural; move deep detail into `references/`.
- Keep diffs minimal and avoid creating low-value support files.
- Do not hand-edit generated outputs when tooling owns them.
- Keep skill names lowercase hyphen-case and <= 64 characters.
- Keep repo anchors portable: prefer repo-relative references for the current repo and logical workspace labels for adjacent repos instead of hardcoded host paths.

## Workflow
1) Confirm scope and what behavior/triggering must remain unchanged.
2) For new skills, scaffold first with `scripts/init_skill.py`; for existing skills, inspect current frontmatter/body and references.
3) Align frontmatter (`name`, `description`, `metadata`) with intended trigger language.
4) Keep body sections concise and actionable, with consistent structure (`Use this skill when`, `Inputs`, `Scope and boundaries`, `Workflow`, `Validation and testing`, `Outputs`, `References`).
5) Place content deliberately:
   - repeated deterministic logic -> `scripts/`
   - long or variant-specific guidance -> `references/`
   - output artifacts/templates -> `assets/`
6) Run validation commands; regenerate catalogs only when skill listings/frontmatter changes require it.
7) Summarize changed files, rationale, and residual risks.

## Skill structure checklist
- Frontmatter and folder name match exactly.
- Description includes both what the skill does and when to use it.
- Body includes one usage section and one workflow section.
- References are linked directly from SKILL.md (avoid deep reference chains).
- Long examples stay in `references/`, not the main body.

## Validation commands
- `python3 "$CODEX_SKILLS/pack-skills/scripts/package_skill.py" <path/to/skill>` (optional packaging flow)

## Agent orchestration
- Delegate only read-only audits (section consistency, trigger-drift checks).
- Keep one owner for final SKILL edits, generation steps, and handoff summary.

## Validation and testing
- Run metadata/catalog sync tooling only when frontmatter or preset listings changed.
- Verify diffs stay within owned skill paths before handoff.

## Outputs
- Minimal SKILL.md/resource diffs that keep trigger intent intact.
- Validation evidence and any required catalog regeneration notes.
- Clear follow-up actions when packaging or extra verification is deferred.

## References
- `references/workflows.md`
- `references/output-patterns.md`
- `scripts/init_skill.py`
- `scripts/quick_validate.py`
- `scripts/package_skill.py`
