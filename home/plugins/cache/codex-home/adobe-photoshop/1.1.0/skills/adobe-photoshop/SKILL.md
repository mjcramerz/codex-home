---
name: adobe-photoshop
description: Coordinate Adobe Photoshop workflows for retouching, compositing, and exporting image assets while keeping handoffs explicit.
metadata:
  version: '1.0'
  short-description: Photoshop image editing workflow
  tags:
  - plugin
  - adobe
  - photoshop
  - image
  - editing
---

# Adobe Photoshop

## Execute the scoped task

1. Identify the actual source assets, requested output, editable format and constraints. Confirm that any named attachment or design exists; do not invent a missing input.

2. Read the selected tool or script contract and establish access to the relevant document, project or account. Keep sensitive source content out of logs and unrelated services.

3. Work on a copy or reversible revision where supported. Preserve required dimensions, metadata, accessibility, editable elements and source fidelity; inspect rendered output rather than relying on file creation alone.

4. Return only artifacts you actually created or changed. Distinguish visual inspection, automated checks and unsupported application-specific behavior; retain required source attribution and licenses.

## Task-specific details and resources

## Use this skill when

- the user needs Adobe Photoshop for retouching, compositing, masking, or color corrections
- image editing requires a UI-first workflow instead of code-only transformations
- output files must be exported in production-ready sizes and formats

## Workflow

1. Confirm source files, target aspect ratios, export formats, and delivery constraints.
2. Use the `adobe-photoshop` app for layer edits, retouching, text overlays, and style refinements.
3. Capture final export names, resolutions, color profile expectations, and any unresolved manual edits.
4. Hand off to `ai-media:imagegen` when the task shifts into generation instead of deterministic editing.

## Outputs

- Photoshop-focused editing plan with explicit input and output files
- Clear handoff notes for follow-up generation, publishing, or QA review

## References

- `references/app-routing.md`
- `references/handoff.md`
