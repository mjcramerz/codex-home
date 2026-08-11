# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-acrobat-forms-sign.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `acrobat-forms-sign` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill acrobat-forms-sign.
- Source PDF and required output variants (fillable, signer-ready, flattened, archival).
- Signer order, signature obligations, and completion policy.
- Submission/export constraints and record-retention expectations.
- Any referenced scripts, assets, or references in the skill.

## Scope
- In: tasks covered by the `acrobat-forms-sign` skill and its resources.
- Out: remote signature-request dispatch unless explicitly requested.

## Action items
[ ] Use skill acrobat-forms-sign and linked resources.
[ ] Confirm signer sequence, required fields, and target output states.
[ ] Preserve original form before applying irreversible operations.
[ ] Execute Acrobat workflow for field prep, fill/sign readiness, and packet outputs.
[ ] Validate final variants by reopening and checking field/signature behavior.
[ ] Record exact outputs (working, signer-ready, archival) and unresolved follow-ups.
[ ] Provide concise handoff note for manual signing or submission steps.

## Testing and validation
- You must follow validation steps in the skill or linked docs.
- You must verify required fields are complete and signer order expectations are documented.
- For flattened/archival outputs, confirm fields are no longer editable and content remains legible.

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
- Incorrect signer order can invalidate packet readiness.
- Irreversible flattening/redaction can remove required editable data.
- Archival copies may fail compliance if metadata/output naming is incomplete.

## Examples

- Example objective: "Prepare signer-ready and archival copies of a multi-party form packet"
- Example validation: "Confirm signer-ready copy is editable and archival copy is flattened"

## Open questions
- None.
