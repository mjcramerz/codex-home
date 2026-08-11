---
name: acrobat-forms-sign
description: Use when the task depends on Adobe Acrobat workflows for fillable forms, field preparation, fill and sign steps, signature-ready packets, or archival copies of signed documents.
metadata:
  version: '1.0'
  short-description: Adobe Acrobat forms, fill and sign, and signature packet workflows
  tags:
  - acrobat-forms-sign
  - adobe-acrobat
  - pdf
  - forms
  - signatures
interface:
  display-name: Acrobat Forms Sign
  short-description: Acrobat forms, fill and sign, and signature packet workflows
  brand-color: '#FF0000'
  default-prompt: Act as the "Acrobat Forms Sign" specialist for Acrobat-based form preparation, fill and sign steps, and signature-ready packet workflows. Keep signer inputs explicit, preserve original files, and report the exact outputs and remaining follow-up.
---

## Use this skill when
- the task is about fillable PDF forms, field preparation, signature-ready packets, or Acrobat fill and sign flows
- the user wants to prepare a clean PDF for signing, flattening, archival storage, or downstream submission
- the workflow depends on Acrobat-specific form tools rather than generic PDF editing

## Inputs
- source PDF and the target output name
- form-field requirements, signer names, and required completion order
- whether the final file should remain fillable, become flattened, or include an archival copy

## Scope and boundaries
- Preserve the original form before changing fields or flattening content.
- Do not send or route signature requests unless the user explicitly asks for that outcome.
- Keep signer order, required fields, and submission expectations explicit before preparing the final packet.
- Call out irreversible steps such as flattening, redaction, or archival export before the final handoff.

## Workflow
1) Confirm whether the task is field prep, form fill, sign-off packaging, or archival export.
2) Inspect the form for required fields, missing labels, signer order, and attachment requirements.
3) Use Acrobat workflows to prepare the document:
   - add or verify fillable fields
   - complete fill-and-sign steps or prepare signer-ready copies
   - create a flattened or archival copy when requested
4) Record the exact outputs: working copy, signer-ready copy, archival copy, and any unresolved manual steps.
5) Validate the final files by reopening them and checking field behavior, page layout, and expected signature state.

## Validation and testing
- Confirm required fields are present and clearly labeled.
- Confirm signer-ready files open cleanly and keep the expected fill/sign behavior.
- If a flattened or archival copy is requested, verify fields are no longer editable and the content remains legible.
- Summarize any manual sign-off, submission, or follow-up steps still required.

## Outputs
- fillable, signer-ready, or flattened PDF files with exact filenames
- concise field/signature checklist for the user
- handoff note describing what remains manual versus fully prepared

## References
- `references/delivery-checklist.md`
- `references/forms-workflows.md`
