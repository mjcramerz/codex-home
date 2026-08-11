---
name: health-adhd-cbt
description: Comprehensive ADHD planning and CBT-based (sometimes requested as "CBD") daily
  templates with PDF generation workflows. Use when generating printable ADHD/CBT worksheets,
  daily planners, impulse-control decision filters, emotion regulation check-ins, or when
  converting template content to PDF/HTML using the bundled scripts and assets.
metadata:
  version: '1.0'
  short-description: ADHD + CBT daily planning PDF templates
  tags:
  - adhd
  - cbt
  - pdf
  - planning
  - templates
interface:
  display-name: HEALTH-ADHD & CBT
  short-description: ADHD + CBT daily planning PDF templates
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#4F32CC'
  default-prompt: Act as the "HEALTH-ADHD & CBT" specialist for "ADHD + CBT daily planning
    PDF templates". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

# HEALTH-ADHD & CBT

## Use this skill when
- generating printable ADHD/CBT worksheets or daily planning packs
- converting bundled templates to HTML/PDF with optional prefill data
- tailoring structured planning artifacts while keeping templates clinically neutral

## Overview
Generate printable ADHD/CBT daily planning PDFs from bundled HTML templates, optionally prefilled from JSON. Keep output practical and low-friction with short timeboxes and small steps.

## Privacy and safety guardrails
- Treat user-provided health notes as sensitive; minimize retention and avoid copying raw content into logs.
- Do not claim diagnosis, treatment, or medical certainty; keep outputs educational and organizational.
- Prefer local/offline rendering paths for sensitive worksheets when feasible.
- Ask for explicit confirmation before embedding highly personal data into persistent files.

## Quick start
Render the original 3-page daily pack as PDF (requires wkhtmltopdf/weasyprint/pandoc):

```bash
python3 scripts/build_daily_pack.py \
  --use-example \
  --out /tmp/adhd-daily-pack.pdf
```

Render a single template to HTML (no PDF engine required):

```bash
python3 scripts/render_template.py \
  --template assets/templates/daily-flow.html \
  --css assets/styles/pdf.css \
  --out /tmp/daily-flow.html
```

Render a custom multi-page pack from JSON config:

```bash
python3 scripts/build_pack.py \
  --config assets/data/pack-config.json \
  --out /tmp/adhd-custom-pack.pdf
```

## Workflow
1) Select a template from `assets/templates/`.
2) Prepare optional data as JSON (see `assets/data/example.json`, `assets/data/focus-example.json`, `assets/data/weekly-example.json`, `assets/data/task-example.json`, `assets/data/monthly-example.json`, `assets/data/appointment-example.json`, `assets/data/sensory-example.json`).
3) Render HTML or PDF with `scripts/render_template.py` or `scripts/build_pack.py`.
4) Review spacing and adjust CSS if needed in `assets/styles/pdf.css`.
5) Export the final PDF and print or share.

## Template inventory
- `daily-flow.html`: AM launch, top 3 outcomes, midday reset, shutdown, micro habits.
- `daily-focus.html`: focus sprint planning, distraction plan, support setup.
- `decisions-impulses.html`: shiny object parking lot, decision filter, email helper.
- `emotions-self-management.html`: CBT thought check, regret reset, HALT basics, wind-down.
- `weekly-plan.html`: weekly outcomes, schedule anchors, energy planning.
- `task-breakdown.html`: task decomposition with tiny steps and blockers.
- `habit-tracker.html`: 2-week habit tracker grid.
- `monthly-review.html`: monthly review, wins, challenges, next priorities.
- `appointment-prep.html`: appointment prep, questions, and follow-ups.
- `sensory-reset.html`: sensory regulation checklist and reset plan.
- `daily-pack.html`: original three pages with page breaks.

## Scripts
- `scripts/render_template.py`: fill placeholders and render HTML/PDF.
- `scripts/build_daily_pack.py`: convenience wrapper for the full pack.
- `scripts/build_pack.py`: build multi-page packs from JSON config.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- Printable HTML/PDF worksheets generated from selected templates.
- Any supporting JSON data payloads used for prefill or pack assembly.
- Reproducible render command(s) and destination paths for the generated artifacts.

## References
- Field map and placeholders: `references/template-fields.md`.
- Pack config format: `references/pack-config.md`.
- Source PDF for alignment: `assets/source/Concise_ADHD_CBT_Daily_Templates_A4_FINAL_COMPLETE_v2.pdf`.

## Notes
- Treat the templates as CBT-informed and intended for education and self-organization, not medical advice.
- Render missing placeholder values as blank lines to keep templates printable and flexible.
- Ask for clarification if a user explicitly wants CBD (cannabidiol) content before editing templates.
