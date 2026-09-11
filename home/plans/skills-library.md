# Skills library plan

Use this plan when you are adding or revising skills in the pack. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when adding or revising skills in the pack.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Each skill has complete frontmatter metadata.
- Skills are discoverable from indexes and overviews.
- Add bundled scripts/references/assets when they materially improve reliability or reuse.

## Scope

- In: runtime skill roots under `$CODEX_HOME/.agents/skills/**` and the managed admin skill root, plus related index links.
- Out: changes to unrelated pack surfaces.

## Files and entry points

- `$CODEX_HOME/.agents/skills`
- the managed admin skill root
- `$CODEX_HOME/index/pack/skills.md`
- `$CODEX_HOME/index/manifest.yml`

## Action items

- [ ] Create or update skill directories and `SKILL.md` files.
- [ ] Ensure `metadata.version`, `metadata.short-description`, and `metadata.tags` are present.
- [ ] Refresh nearby runtime catalog docs or metadata after changing a skill.
- [ ] Validate the affected runtime references under `$CODEX_HOME/.agents/skills` or the managed admin skill root.

## Testing and validation

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Capture expected outcomes and acceptance criteria for each validation step.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Confirm migration/backfill or feature-flag sequencing when applicable.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## Risks and edge cases

- Missing metadata or inconsistent naming.
- Skills not referenced in discovery docs.

## Examples

- Example objective: "Add or revise a runtime skill and keep its metadata plus discovery surfaces aligned."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
