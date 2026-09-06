# Security Context Checkpoint

Create a compact, evidence-led handoff for the next authorized security or
coding agent. Preserve scope and safety boundaries as carefully as technical
findings.

Output Markdown with these exact sections:

## Authorized Objective
- Requested security outcome, explicit authorization, in-scope assets, and
  non-goals.
- Applicable instructions, legal or operational boundaries, and approval state
  for any potentially disruptive action.

## Evidence and State
- Verified observations, affected paths or systems, relevant revisions,
  commands, timestamps, and sanitized logs or indicators.
- Separate confirmed facts, hypotheses, false positives, and unknowns.

## Work Completed
- Read-only checks, changes, mitigations, and validations performed.
- Exact blast-radius or rollback considerations for every mutation.

## Remaining Work
1. Safest next authorized action and required preconditions.
2. Required validation, containment, remediation, or reporting work.
3. Blockers, missing authorization, credentials, or owner decisions.

Rules:
- Do not include secrets, exploit payloads, credentials, private data, or
  concealed reasoning.
- Do not expand scope or imply authorization that was not explicit.
- Preserve evidence integrity and never claim a vulnerability, remediation, or
  test result without direct support.
