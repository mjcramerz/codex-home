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

## Use this skill when
- the task needs Acrobat to open, organize, annotate, or export an existing PDF
- the user wants a UI-driven PDF workflow instead of a code-generated document flow
- you need a clean handoff between Acrobat work and local `document-artifacts` skills

## Workflow
1) Confirm the source files, expected output PDF, and any page-order or annotation requirements.
2) Use the `adobe-acrobat` app for page organization, rotation, merging, splitting, comments, and export.
3) Capture the resulting filenames, page counts, review notes, and any unresolved manual steps.
4) If the task shifts into generation or layout repair, hand off to `document-artifacts:pdf` or `document-artifacts:doc`.

## Outputs
- Acrobat-ready PDF review or organization plan
- Clear handoff notes for follow-up editing, signing, or export work

## References
- `references/app-routing.md`
- `references/pdf-handoff.md`
