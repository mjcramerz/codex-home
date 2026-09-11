---
name: acrobat-reader
description: Coordinate Adobe Acrobat workflows for reading, organizing, annotating, and exporting PDFs while keeping handoffs to local document tooling explicit.
metadata:
  version: '1.0'
  short-description: Acrobat PDF review and organization workflow
  tags:
  - plugin
  - acrobat
  - pdf
  - review
  - documents
---

# Acrobat Reader

## Execute the scoped task

1. Identify the actual source assets, requested output, editable format and constraints. Confirm that any named attachment or design exists; do not invent a missing input.

2. Read the selected tool or script contract and establish access to the relevant document, project or account. Keep sensitive source content out of logs and unrelated services.

3. Work on a copy or reversible revision where supported. Preserve required dimensions, metadata, accessibility, editable elements and source fidelity; inspect rendered output rather than relying on file creation alone.

4. Return only artifacts you actually created or changed. Distinguish visual inspection, automated checks and unsupported application-specific behavior; retain required source attribution and licenses.

## Task-specific details and resources

## Use this skill when

- the task needs Acrobat to open, organize, annotate, or export an existing PDF
- the user wants a UI-driven PDF workflow instead of a code-generated document flow
- you need a clean handoff between Acrobat work and local `document-artifacts` skills

## Workflow

1. Confirm the source files, expected output PDF, and any page-order or annotation requirements.
2. Use the `adobe-acrobat` app for page organization, rotation, merging, splitting, comments, and export.
3. Capture the resulting filenames, page counts, review notes, and any unresolved manual steps.
4. If the task shifts into generation or layout repair, hand off to `document-artifacts:pdf` or `document-artifacts:doc`.

## Outputs

- Acrobat-ready PDF review or organization plan
- Clear handoff notes for follow-up editing, signing, or export work

## References

- `references/app-routing.md`
- `references/pdf-handoff.md`
