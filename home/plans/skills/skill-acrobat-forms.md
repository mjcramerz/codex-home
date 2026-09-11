# Acrobat forms plan

Use this plan when you applying or updating the `acrobat-forms` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `acrobat-forms` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `acrobat-forms` skill only when its trigger matches this task and the skill is available.
- Source form PDF path and target output file naming.
- Required field set, signer roles, and completion deadlines.
- Submission requirements (fillable, flattened, or both).
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `acrobat-forms` skill and its resources.
- Out: signature-routing workflows that require explicit send/approval orchestration outside local preparation.

## Action items

- [ ] Use skill acrobat-forms and linked resources.
- [ ] Confirm form objective, source file, and required signer/data inputs.
- [ ] Inventory mandatory fields and identify missing or ambiguous form sections.
- [ ] Execute Acrobat form workflow (field prep, fill-and-sign, review, export).
- [ ] Validate required fields, signatures, dates, and attachment expectations.
- [ ] Capture missing-input checklist and unresolved manual signer actions.
- [ ] Produce final handoff summary with exact filenames and state.

## Testing and validation

- Follow validation steps in the skill or linked docs.
- Re-open output PDFs and verify field behavior (editable vs flattened as requested).
- Confirm mandatory fields are complete and signatures render correctly.

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

- Hidden or malformed form fields can cause incomplete submissions.
- Flattening too early can prevent required corrections.
- Time-sensitive signatures can expire before delivery.

## Examples

- Example objective: "Prepare a fillable onboarding packet and create a signed-ready copy"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
