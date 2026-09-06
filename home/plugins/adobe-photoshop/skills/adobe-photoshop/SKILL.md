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

## Use this skill when
- the user needs Adobe Photoshop for retouching, compositing, masking, or color corrections
- image editing requires a UI-first workflow instead of code-only transformations
- output files must be exported in production-ready sizes and formats

## Workflow
1) Confirm source files, target aspect ratios, export formats, and delivery constraints.
2) Use the `adobe-photoshop` app for layer edits, retouching, text overlays, and style refinements.
3) Capture final export names, resolutions, color profile expectations, and any unresolved manual edits.
4) Hand off to `ai-media:imagegen` when the task shifts into generation instead of deterministic editing.

## Outputs
- Photoshop-focused editing plan with explicit input and output files
- Clear handoff notes for follow-up generation, publishing, or QA review

## References
- `references/app-routing.md`
- `references/handoff.md`
