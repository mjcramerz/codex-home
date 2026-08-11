# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-adobe-photoshop.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `adobe-photoshop` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill adobe-photoshop.
- Source image paths, edit intent, and target output variants.
- Export requirements (dimensions, format, compression, color profile).
- Brand constraints, style references, and approval requirements.
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `adobe-photoshop` skill and its resources.
- Out: net-new image generation workflows outside deterministic Photoshop editing tasks.

## Action items
[ ] Use skill adobe-photoshop and linked resources.
[ ] Confirm source assets, ownership/license constraints, and required output variants.
[ ] Capture exact transformation intent (retouch, compositing, masking, color, text overlays).
[ ] Define export matrix (per-file dimensions, format, quality/compression, profile).
[ ] Execute the skill workflow and record explicit handoff notes for unresolved edits.
[ ] Validate outputs against dimensions, naming conventions, and visual acceptance criteria.
[ ] Update links/backlinks or task notes if additional downstream packaging is required.

## Testing and validation
- You must follow validation steps in the skill or linked docs.
- You must verify output files open correctly and match expected dimensions and format.
- You must validate that final filenames are deterministic and mapped to the requested variants.

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
- Missing or low-quality source assets can block deterministic edits.
- Color profile mismatches can create inconsistent outputs across tools.
- Export naming drift can break downstream automation or review workflows.
- App availability or permissions can require explicit fallback handoff.

## Examples

- Example objective: "Retouch and export three hero images for web and social variants"
- Example validation: "Check all outputs for expected dimensions and file format"

## Open questions
- None.
