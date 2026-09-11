# Health adhd cbt plan

Use this plan when you applying or updating the `health-adhd-cbt` skill. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when applying or updating the `health-adhd-cbt` skill.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- Read the `health-adhd-cbt` skill only when its trigger matches this task and the skill is available.
- health-adhd-cbt skill asset `assets/templates/`
- health-adhd-cbt skill asset `assets/styles/pdf.css`
- health-adhd-cbt skill asset `assets/data/pack-config.json`

## Scope

- In: generating ADHD/CBT printable templates, PDF packs, or updating the health-adhd-cbt skill assets/scripts.
- Out: unrelated mental health guidance or medical advice.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Use skill health-adhd-cbt and linked references.
- [ ] Confirm whether the user means CBT or CBD when ambiguous.
- [ ] Select templates and data sources (JSON or inline).
- [ ] Render HTML/PDF using `render_template.py` or `build_pack.py`.
- [ ] Review layout/spacing and adjust CSS if needed.

## Testing and validation

- Run a sample render to HTML to confirm placeholders fill as expected.
- If available, generate a PDF with wkhtmltopdf/weasyprint/pandoc.

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

- Missing PDF engine (fallback to HTML).
- Oversized data/JSON causing output truncation.
- Misinterpretation of "CBD" vs "CBT".

## Examples

- Example objective: "Generate a 5-day ADHD daily pack with a weekly plan page."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
