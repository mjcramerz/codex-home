# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-acrobat-reader.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `acrobat-reader` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill acrobat-reader.
- Source PDF paths and expected output artifact names.
- You must document objectives (read, organize, annotate, split/merge, export).
- Page-order constraints, annotation requirements, and review deadlines.
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `acrobat-reader` skill and its resources.
- Out: net-new document generation/layout-authoring tasks better handled by `document-artifacts:*`.

## Action items
[ ] Use skill acrobat-reader and linked resources.
[ ] Confirm source files, target outputs, and required PDF operations.
[ ] Define annotation/comment conventions and ownership for review artifacts.
[ ] Execute Acrobat reading/organization workflow (open, rotate, merge/split, annotate, export).
[ ] Capture resulting filenames, page counts, and unresolved manual follow-up.
[ ] Validate output readability, page order, and annotation persistence.
[ ] Hand off to downstream owner or `document-artifacts` skill when needed.

## Testing and validation
- You must follow validation steps in the skill or linked docs.
- Re-open outputs and verify page order, orientation, and expected comments.
- You must confirm exports match requested format and naming conventions.

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
- Corrupted or password-protected PDFs can block intended review steps.
- Mixed page sizes/orientations can cause export or print mismatch.
- Annotation layer flattening can remove expected editable comments.

## Examples

- Example objective: "Organize a 120-page contract packet and add reviewer comments"
- Example validation: "Verify page order and exported comment summary"

## Open questions
- None.
