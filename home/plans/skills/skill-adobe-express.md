# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-adobe-express.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `adobe-express` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill adobe-express.
- Campaign goal, audience, and required channel outputs.
- Copy constraints, brand system requirements, and template preferences.
- Export targets (platform sizes, formats, and naming rules).
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `adobe-express` skill and its resources.
- Out: advanced pixel-level retouch/compositing better handled in Photoshop workflows.

## Action items
[ ] Use skill adobe-express and linked resources.
[ ] Confirm target channels, asset dimensions, and delivery deadlines.
[ ] Validate copy, CTA, and brand constraints before producing variants.
[ ] Select template direction and define per-channel adaptation requirements.
[ ] Execute the skill workflow and produce a deterministic export set.
[ ] Validate outputs for channel dimensions, readability, and filename conventions.
[ ] Capture handoff notes for any downstream Photoshop or document-packaging steps.

## Testing and validation
- You must follow validation steps in the skill or linked docs.
- You must verify exported assets match required platform dimensions and visual hierarchy.
- You must confirm copy fidelity and brand compliance across all generated variants.

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
- Missing channel specs can cause incorrect export dimensions.
- Template constraints can conflict with dense copy requirements.
- Inconsistent branding inputs can produce non-compliant creative variants.
- Last-minute copy changes can require full variant regeneration.

## Examples

- Example objective: "Create launch graphics for LinkedIn, Instagram, and email header"
- Example validation: "Confirm each export size matches channel spec and naming convention"

## Open questions
- None.
