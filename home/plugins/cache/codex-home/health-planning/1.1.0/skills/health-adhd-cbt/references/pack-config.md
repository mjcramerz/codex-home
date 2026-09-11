---
title: Pack config format (JSON)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- health-adhd-cbt
- references
- pack-config-md
- pack-config
- admin
updated: '2026-02-20'
---
# Pack config format (JSON)

Use this file format with `$CODEX_HOME/plugins/cache/codex-home/health-planning/1.0.0/skills/health-adhd-cbt/scripts/build_pack.py` from the skill root.

## Top-level fields
- `page_size` (optional): PDF page size token (default `A4`; examples: `A4`, `Letter`).
- `margin` (optional): PDF margin with units (default `14mm`; examples: `10mm`, `0.5in`).
- `css` (optional): CSS path relative to the skill root `$CODEX_HOME/plugins/cache/codex-home/health-planning/1.0.0/skills/health-adhd-cbt/assets/` directory (must not escape root) or an absolute path.
- `pages` (required): array of page entries (see below).

## Page entry fields
- `template` (required): template filename or path. If no extension, `.html` is added.
  Relative paths are resolved under `$CODEX_HOME/plugins/cache/codex-home/health-planning/1.0.0/skills/health-adhd-cbt/assets/templates/` and may not escape that directory.
- `data` (optional): inline object of placeholder values.
- `data_file` (optional): path to JSON file of placeholder values.
- `data` and `data_file` are mutually exclusive for each page entry.
- `repeat` (optional): integer 1-31, repeat page multiple times.
- `start_date` (optional): `YYYY-MM-DD` start date for repeat pages.
- `force_date` (optional): true to override `day`/`date` even if provided in data.

## Limits and validation
- Max config size: 1,000,000 bytes.
- Max rendered pages per pack: 200 (after `repeat` expansion).
- Invalid page-size or margin formats fail closed before rendering.

## Example
```json
{
  "page_size": "A4",
  "css": "styles/pdf.css",
  "pages": [
    {
      "template": "daily-flow.html",
      "repeat": 5,
      "start_date": "2026-01-15",
      "force_date": true
    },
    {
      "template": "weekly-plan.html",
      "data": {"weekly_theme": "stability"}
    }
  ]
}
```
