---
name: hook-behavior-audit
description: Use this skill to review startup, resume, and stop hooks for schema compliance,
  blocking behavior, repo-context quality, and validation-gate correctness. Use this
  skill when you need to audit hook UX, guardrails, or lifecycle automation.
metadata:
  version: '1.0'
  short-description: Audit startup/resume/stop hooks and lifecycle guardrails
  tags:
  - audit
  - hooks
  - lifecycle
  - ux
interface:
  display-name: AUDIT-Hook Behavior
  short-description: Audit startup/resume/stop hooks and lifecycle guardrails
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#8B5CF6'
  default-prompt: Act as the "AUDIT-Hook Behavior" specialist for "Audit startup/resume/stop
    hooks and lifecycle guardrails". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Hook Behavior Audit

## Workflow

1. Trace the registered event through hooks.json to the actual executable. Verify event-specific input/output against the selected Codex version.

2. Check timeout, payload/output bounds, exit behavior, symlink/path handling and malformed-input behavior. Keep stdout valid JSON and stderr redacted.

3. Ensure context contains only bounded repository hints and relevant guidance, never config schemas, credentials, transcripts or raw tool results.

4. Verify permission hooks never turn context hints into blanket approval, and stop/compaction hooks neither invent validation success nor cause continuation loops.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
