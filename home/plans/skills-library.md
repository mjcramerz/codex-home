# Plan
Purpose: tell the Codex coding agent how to use `plans/skills-library.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when adding or revising skills in the pack.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Requirements
- Each skill has complete frontmatter metadata.
- Skills are discoverable from indexes and overviews.
- You must add bundled scripts/references/assets when they materially improve reliability or reuse.

## Scope
- In: runtime skill roots under `$CODEX_HOME/.agents/skills/**` and the managed admin skill root, plus related index links.
- Out: changes to unrelated pack surfaces.

## Files and entry points
- `$CODEX_HOME/.agents/skills`
- the managed admin skill root
- `$CODEX_HOME/index/pack/skills.md`
- `$CODEX_HOME/index/manifest.yml`

## Action items
[ ] Create or update skill directories and `SKILL.md` files.
[ ] Ensure `metadata.version`, `metadata.short-description`, and `metadata.tags` are present.
[ ] Refresh nearby runtime catalog docs or metadata after changing a skill.
[ ] Validate the affected runtime references under `$CODEX_HOME/.agents/skills` or the managed admin skill root.

## Testing and validation

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- You must record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints
- You must define fast-path and deep validation commands before making changes.
- You must capture expected outcomes and acceptance criteria for each validation step.
- You must re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints
- You must document rollout order, blast-radius controls, and rollback conditions.
- You must confirm migration/backfill or feature-flag sequencing when applicable.
- You must record post-deploy verification owners and evidence.

## Multi-agent handoff
- Coordinator hands off scope, constraints, and stop condition with the target entrypoint.
- Executor reports touched files, commands run, evidence, blockers, and next action.
- Receiving agent acknowledges handoff completeness before continuing execution.

## Risks and edge cases
- Missing metadata or inconsistent naming.
- Skills not referenced in discovery docs.

## Examples

- Example objective: "Add or revise a runtime skill and keep its metadata plus discovery surfaces aligned."
- Example validation: "python3 -m unittest tests.test_skill_catalog_contract"

## Open questions
- None.
