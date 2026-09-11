---
name: quality-code-review
description: Use this skill to perform high-rigor code review focused on correctness,
  regressions, security, performance, and test coverage. Use when the user asks for
  a review, audit, risk assessment, or PR quality gate.
metadata:
  version: '1.1'
  short-description: Rigorous code review for correctness, security, performance,
    regressions, and test coverage
  tags:
  - code-review
  - security
  - testing
  - performance
interface:
  display-name: QUALITY-Code Review
  short-description: Rigorous code review for correctness, security, performance,
    regressions, and test coverage
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC4C'
  default-prompt: 'Act as the "QUALITY-Code Review" specialist for "High-rigor code
    review skill: intent alignment, correctness, security, performance, and reproducibility
    checks with actionable output". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.'
---

# Quality Code Review

## Workflow

1. Read the actual diff, relevant callers and existing checks before judging intent. Focus on actionable regressions introduced by the change.

2. Prioritize correctness, security, data loss, compatibility and operational failure modes. Separate confirmed findings from questions.

3. Tie each finding to the smallest relevant path/line range, triggering conditions, impact and a concrete correction. Avoid style-only noise outside scope.

4. Report only checks actually run and return the requested review format; do not modify code unless the task includes remediation.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/docs/security/review-hardening.md`
- `$CODEX_HOME/docs/workflows/testing.md`
- `$CODEX_HOME/docs/perf/overview.md`
- `$CODEX_HOME/docs/workflows/code-review.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
