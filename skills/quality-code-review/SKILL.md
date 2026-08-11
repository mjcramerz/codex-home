---
name: quality-code-review
description: Perform high-rigor code review focused on correctness, regressions, security,
  performance, and test coverage. Use when the user asks for a review, audit, risk assessment,
  or PR quality gate.
metadata:
  version: '1.1'
  short-description: 'High-rigor code review skill: intent alignment, correctness, security,
    performance, and reproducibility checks with actionable output'
  tags:
  - code-review
  - security
  - testing
  - performance
interface:
  display-name: QUALITY-Code Review
  short-description: 'High-rigor code review skill: intent alignment, correctness, security,
    performance, and reproducibility checks with actionable output'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC4C'
  default-prompt: 'Act as the "QUALITY-Code Review" specialist for "High-rigor code review
    skill: intent alignment, correctness, security, performance, and reproducibility checks
    with actionable output". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.'
---

## Use this skill when
- auditing pull requests for correctness, regressions, and security issues
- producing severity-ranked findings and concrete remediation guidance
- validating whether tests and CI evidence are sufficient for merge

## Workflow
1) Scope and context:
   - Identify the review target (branch/commit range/files) and expected intent.
   - Confirm risk profile (security-sensitive, user-facing, data-destructive, release-critical).
2) Findings-first analysis:
   - Enumerate concrete issues before summaries.
   - Order findings by severity (`critical`, `high`, `medium`, `low`).
   - Include file and line references for each finding.
3) Behavioral validation:
   - Check correctness/regression risk, authz boundaries, timeout/retry bounds, and error-path handling.
   - Validate tests/linters/build evidence against touched code paths.
4) Actionability pass:
   - Provide clear remediation guidance for each finding.
   - Call out missing tests, ambiguous assumptions, and required follow-up checks.
5) Final report:
   - Keep summary brief and secondary to findings.
   - Explicitly state when no findings are identified and list residual risks/testing gaps.

## Review output format
1) Findings (ordered by severity with file/line references)
2) Open questions / assumptions
3) Brief change summary
4) Validation evidence and missing checks
5) Residual risks / follow-up recommendations

## Review heuristics
- Minimize diff surface area
- Validate error handling paths
- Look for injection and boundary violations
- Ensure timeouts and limits
- Ensure lockfiles and audits when deps change

## Security and reliability checks (quick)
- Identify trust boundaries and validate all inputs at those boundaries.
- Ensure secrets are not logged and errors do not leak internal details.
- Check for unbounded loops, unbounded retries, and missing timeouts on I/O.
- For web/API: request body limits, rate limiting, SSRF defenses where outbound fetch exists.

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
- A structured review with severities and actionable fixes.
- A minimal test plan and risk summary.
- Callout of any behavior changes or backward-compat risks.

## References
- `$CODEX_HOME/docs/security/review-hardening.md`
- `$CODEX_HOME/docs/workflows/testing.md`
- `$CODEX_HOME/docs/perf/overview.md`
- `$CODEX_HOME/docs/workflows/code-review.md`
