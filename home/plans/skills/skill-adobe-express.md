# Adobe express plan

Use this plan when you applying or updating the `adobe-express` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `adobe-express` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `adobe-express` skill only when its trigger matches this task and the skill is available.
- Campaign goal, audience, and required channel outputs.
- Copy constraints, brand system requirements, and template preferences.
- Export targets (platform sizes, formats, and naming rules).
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `adobe-express` skill and its resources.
- Out: advanced pixel-level retouch/compositing better handled in Photoshop workflows.

## Action items

- [ ] Use skill adobe-express and linked resources.
- [ ] Confirm target channels, asset dimensions, and delivery deadlines.
- [ ] Validate copy, CTA, and brand constraints before producing variants.
- [ ] Select template direction and define per-channel adaptation requirements.
- [ ] Execute the skill workflow and produce a deterministic export set.
- [ ] Validate outputs for channel dimensions, readability, and filename conventions.
- [ ] Capture handoff notes for any downstream Photoshop or document-packaging steps.

## Testing and validation

- Follow validation steps in the skill or linked docs.
- Verify exported assets match required platform dimensions and visual hierarchy.
- Confirm copy fidelity and brand compliance across all generated variants.

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

- Missing channel specs can cause incorrect export dimensions.
- Template constraints can conflict with dense copy requirements.
- Inconsistent branding inputs can produce non-compliant creative variants.
- Last-minute copy changes can require full variant regeneration.

## Examples

- Example objective: "Create launch graphics for LinkedIn, Instagram, and email header"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
