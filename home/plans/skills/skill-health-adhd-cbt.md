# Plan
Purpose: tell the Codex coding agent how to use `plans/skills/skill-health-adhd-cbt.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when applying or updating the `health-adhd-cbt` skill.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/skills/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- You must use skill health-adhd-cbt.
- health-adhd-cbt skill asset `assets/templates/`
- health-adhd-cbt skill asset `assets/styles/pdf.css`
- health-adhd-cbt skill asset `assets/data/pack-config.json`

## Scope
- In: generating ADHD/CBT printable templates, PDF packs, or updating the health-adhd-cbt skill assets/scripts.
- Out: unrelated mental health guidance or medical advice.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Use skill health-adhd-cbt and linked references.
[ ] Confirm whether the user means CBT or CBD when ambiguous.
[ ] Select templates and data sources (JSON or inline).
[ ] Render HTML/PDF using `render_template.py` or `build_pack.py`.
[ ] Review layout/spacing and adjust CSS if needed.

## Testing and validation
- You must run a sample render to HTML to confirm placeholders fill as expected.
- If available, generate a PDF with wkhtmltopdf/weasyprint/pandoc.

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
- Missing PDF engine (fallback to HTML).
- Oversized data/JSON causing output truncation.
- Misinterpretation of "CBD" vs "CBT".

## Examples
- Example objective: "Generate a 5-day ADHD daily pack with a weekly plan page."
- Example validation: `python3 "$CODEX_HOME/plugins/cache/<marketplace>/health-planning/<version>/skills/health-adhd-cbt/scripts/build_pack.py" --config "$CODEX_HOME/plugins/cache/<marketplace>/health-planning/<version>/skills/health-adhd-cbt/assets/data/pack-config.json" --out "${TMPDIR:-/tmp}/adhd-pack.html"`

## Open questions
- None.
