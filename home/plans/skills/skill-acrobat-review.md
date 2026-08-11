# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-acrobat-review.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `acrobat-review` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill acrobat-review.
- Baseline and revised PDF paths.
- Review objective (compare versions, consolidate comments, action extraction).
- Reviewer roles, deadlines, and expected handoff format.
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `acrobat-review` skill and its resources.
- Out: upstream content-authoring changes that should occur in source document systems.

## Action items
[ ] Use skill acrobat-review and linked resources.
[ ] Confirm baseline/revision files and review goals.
[ ] Define decision criteria for material vs cosmetic differences.
[ ] Execute Acrobat compare/comment workflow and consolidate markup.
[ ] Summarize differences, unresolved questions, and required follow-up actions.
[ ] Export reviewed artifact(s) and collaborator-ready handoff notes.
[ ] Validate handoff package completeness (files, summary, owners, next steps).

## Testing and validation
- You must follow validation steps in the skill or linked docs.
- Re-open compared outputs to verify comment visibility and revision markers.
- You must confirm action-item summary aligns with visible markup and file evidence.

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
- Baseline mismatch can invalidate comparison findings.
- Dense annotation sets can hide unresolved critical comments.
- Exported summaries can miss context if reviewer ownership is unclear.

## Examples

- Example objective: "Compare two policy PDFs and produce a comment-driven action summary"
- Example validation: "Cross-check action summary against comment and diff markers"

## Open questions
- None.
