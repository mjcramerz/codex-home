# Review Context Checkpoint

Create an evidence-first handoff for the next review agent. Preserve review
scope, finding quality, and the exact state of verification.

Output Markdown with these exact sections:

## Review Scope
- Requested review objective, comparison base or revision range, in-scope
  paths, and applicable repository instructions.

## Evidence Reviewed
- Files, commits, tests, runtime behavior, and documentation examined.
- What was not inspected and why.

## Findings
- Each confirmed finding with severity, affected location, concrete impact, and
  evidence or reproduction.
- Clearly separate resolved findings, suspected issues, and non-findings.

## Remaining Review
1. Next highest-value inspection or validation command.
2. Required follow-up before declaring the review complete.
3. Residual risks, coverage gaps, and questions for the author.

Rules:
- Do not invent defects or report style preferences as correctness findings.
- Do not claim a check passed unless it was run.
- Keep secrets, private reasoning, and irrelevant diffs out of the handoff.
