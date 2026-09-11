# Adobe photoshop plan

Use this plan when you applying or updating the `adobe-photoshop` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `adobe-photoshop` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `adobe-photoshop` skill only when its trigger matches this task and the skill is available.
- Source image paths, edit intent, and target output variants.
- Export requirements (dimensions, format, compression, color profile).
- Brand constraints, style references, and approval requirements.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `adobe-photoshop` skill and its resources.
- Out: net-new image generation workflows outside deterministic Photoshop editing tasks.

## Action items

- [ ] Use skill adobe-photoshop and linked resources.
- [ ] Confirm source assets, ownership/license constraints, and required output variants.
- [ ] Capture exact transformation intent (retouch, compositing, masking, color, text overlays).
- [ ] Define export matrix (per-file dimensions, format, quality/compression, profile).
- [ ] Execute the skill workflow and record explicit handoff notes for unresolved edits.
- [ ] Validate outputs against dimensions, naming conventions, and visual acceptance criteria.
- [ ] Update links/backlinks or task notes if additional downstream packaging is required.

## Testing and validation

- Follow validation steps in the skill or linked docs.
- Verify output files open correctly and match expected dimensions and format.
- Validate that final filenames are deterministic and mapped to the requested variants.

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

- Missing or low-quality source assets can block deterministic edits.
- Color profile mismatches can create inconsistent outputs across tools.
- Export naming drift can break downstream automation or review workflows.
- App availability or permissions can require explicit fallback handoff.

## Examples

- Example objective: "Retouch and export three hero images for web and social variants"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
