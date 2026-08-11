# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-acrobat-forms.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `acrobat-forms` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill acrobat-forms.
- Source form PDF path and target output file naming.
- Required field set, signer roles, and completion deadlines.
- Submission requirements (fillable, flattened, or both).
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `acrobat-forms` skill and its resources.
- Out: signature-routing workflows that require explicit send/approval orchestration outside local preparation.

## Action items
[ ] Use skill acrobat-forms and linked resources.
[ ] Confirm form objective, source file, and required signer/data inputs.
[ ] Inventory mandatory fields and identify missing or ambiguous form sections.
[ ] Execute Acrobat form workflow (field prep, fill-and-sign, review, export).
[ ] Validate required fields, signatures, dates, and attachment expectations.
[ ] Capture missing-input checklist and unresolved manual signer actions.
[ ] Produce final handoff summary with exact filenames and state.

## Testing and validation
- You must follow validation steps in the skill or linked docs.
- Re-open output PDFs and verify field behavior (editable vs flattened as requested).
- You must confirm mandatory fields are complete and signatures render correctly.

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
- Hidden or malformed form fields can cause incomplete submissions.
- Flattening too early can prevent required corrections.
- Time-sensitive signatures can expire before delivery.

## Examples

- Example objective: "Prepare a fillable onboarding packet and create a signed-ready copy"
- Example validation: "Verify all required fields and signature blocks are present and legible"

## Open questions
- None.
