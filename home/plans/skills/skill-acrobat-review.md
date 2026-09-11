# Acrobat review plan

Use this plan when you applying or updating the `acrobat-review` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `acrobat-review` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `acrobat-review` skill only when its trigger matches this task and the skill is available.
- Baseline and revised PDF paths.
- Review objective (compare versions, consolidate comments, action extraction).
- Reviewer roles, deadlines, and expected handoff format.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `acrobat-review` skill and its resources.
- Out: upstream content-authoring changes that should occur in source document systems.

## Action items

- [ ] Use skill acrobat-review and linked resources.
- [ ] Confirm baseline/revision files and review goals.
- [ ] Define decision criteria for material vs cosmetic differences.
- [ ] Execute Acrobat compare/comment workflow and consolidate markup.
- [ ] Summarize differences, unresolved questions, and required follow-up actions.
- [ ] Export reviewed artifact(s) and collaborator-ready handoff notes.
- [ ] Validate handoff package completeness (files, summary, owners, next steps).

## Testing and validation

- Follow validation steps in the skill or linked docs.
- Re-open compared outputs to verify comment visibility and revision markers.
- Confirm action-item summary aligns with visible markup and file evidence.

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

- Baseline mismatch can invalidate comparison findings.
- Dense annotation sets can hide unresolved critical comments.
- Exported summaries can miss context if reviewer ownership is unclear.

## Examples

- Example objective: "Compare two policy PDFs and produce a comment-driven action summary"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
