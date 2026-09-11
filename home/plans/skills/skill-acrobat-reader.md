# Acrobat reader plan

Use this plan when you applying or updating the `acrobat-reader` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `acrobat-reader` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `acrobat-reader` skill only when its trigger matches this task and the skill is available.
- Source PDF paths and expected output artifact names.
- Document objectives (read, organize, annotate, split/merge, export).
- Page-order constraints, annotation requirements, and review deadlines.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `acrobat-reader` skill and its resources.
- Out: net-new document generation/layout-authoring tasks better handled by `document-artifacts:*`.

## Action items

- [ ] Use skill acrobat-reader and linked resources.
- [ ] Confirm source files, target outputs, and required PDF operations.
- [ ] Define annotation/comment conventions and ownership for review artifacts.
- [ ] Execute Acrobat reading/organization workflow (open, rotate, merge/split, annotate, export).
- [ ] Capture resulting filenames, page counts, and unresolved manual follow-up.
- [ ] Validate output readability, page order, and annotation persistence.
- [ ] Hand off to downstream owner or `document-artifacts` skill when needed.

## Testing and validation

- Follow validation steps in the skill or linked docs.
- Re-open outputs and verify page order, orientation, and expected comments.
- Confirm exports match requested format and naming conventions.

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

- Corrupted or password-protected PDFs can block intended review steps.
- Mixed page sizes/orientations can cause export or print mismatch.
- Annotation layer flattening can remove expected editable comments.

## Examples

- Example objective: "Organize a 120-page contract packet and add reviewer comments"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
