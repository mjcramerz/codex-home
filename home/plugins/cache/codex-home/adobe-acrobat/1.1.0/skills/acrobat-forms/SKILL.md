---
name: acrobat-forms
description: Run Adobe Acrobat form, fill-and-sign, and field QA workflows with explicit intake, validation, and handoff steps.
metadata:
  version: '1.0'
  short-description: Acrobat forms and fill-sign workflow
  tags:
  - plugin
  - acrobat
  - pdf
  - forms
  - signature
---

# Acrobat Forms

## Execute the scoped task

1. Identify the actual source assets, requested output, editable format and constraints. Confirm that any named attachment or design exists; do not invent a missing input.

2. Read the selected tool or script contract and establish access to the relevant document, project or account. Keep sensitive source content out of logs and unrelated services.

3. Work on a copy or reversible revision where supported. Preserve required dimensions, metadata, accessibility, editable elements and source fidelity; inspect rendered output rather than relying on file creation alone.

4. Return only artifacts you actually created or changed. Distinguish visual inspection, automated checks and unsupported application-specific behavior; retain required source attribution and licenses.

## Task-specific details and resources

## Use this skill when

- the user needs to fill, sign, or review PDF forms in Acrobat
- the task depends on field mapping, required inputs, or submission readiness
- the output must stay inside an Acrobat-friendly fill-and-sign workflow

## Workflow

1. Gather the source form, required inputs, signer roles, and deadline or submission rules.
2. Use the `adobe-acrobat` app for form filling, fill-and-sign, field review, and export.
3. Validate required fields, signatures, dates, and attachment expectations before handoff.
4. Record any missing data, blocked fields, or manual signer actions that remain.

## Outputs

- Completed or partially completed Acrobat form packet
- Missing-input checklist and signer handoff summary

## References

- `references/form-intake.md`
- `references/form-qa-checklist.md`
