# Acrobat forms sign plan

Use this plan when you applying or updating the `acrobat-forms-sign` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `acrobat-forms-sign` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `acrobat-forms-sign` skill only when its trigger matches this task and the skill is available.
- Source PDF and required output variants (fillable, signer-ready, flattened, archival).
- Signer order, signature obligations, and completion policy.
- Submission/export constraints and record-retention expectations.
- Any referenced scripts, assets, or references in the skill.

## Scope

- In: tasks covered by the `acrobat-forms-sign` skill and its resources.
- Out: remote signature-request dispatch unless explicitly requested.

## Action items

- [ ] Use skill acrobat-forms-sign and linked resources.
- [ ] Confirm signer sequence, required fields, and target output states.
- [ ] Preserve original form before applying irreversible operations.
- [ ] Execute Acrobat workflow for field prep, fill/sign readiness, and packet outputs.
- [ ] Validate final variants by reopening and checking field/signature behavior.
- [ ] Record exact outputs (working, signer-ready, archival) and unresolved follow-ups.
- [ ] Provide concise handoff note for manual signing or submission steps.

## Testing and validation

- Follow validation steps in the skill or linked docs.
- Verify required fields are complete and signer order expectations are documented.
- For flattened/archival outputs, confirm fields are no longer editable and content remains legible.

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

- Incorrect signer order can invalidate packet readiness.
- Irreversible flattening/redaction can remove required editable data.
- Archival copies may fail compliance if metadata/output naming is incomplete.

## Examples

- Example objective: "Prepare signer-ready and archival copies of a multi-party form packet"
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
