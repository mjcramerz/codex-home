---
name: api-reference-research
description: Use this skill for translate API docs into concrete integration checklists.
metadata:
  version: '1.0'
  short-description: API Reference Research
  tags:
  - plugin
  - research
  - api
---

# API Reference Research

## Execute the scoped task

1. Resolve the exact resource, account or repository required by the task. Use a relevant read to obtain missing IDs; do not infer access or authorization from a bundled manifest.

2. Inspect the advertised tool contract or the directly linked reference before choosing an operation. Verify version-sensitive behavior against the provider's primary documentation when necessary.

3. Perform the smallest authorized operation, preserving existing data and unrelated work. Confirm the destination and side effects before writes, uploads, notifications or publication.

4. Check the actual result and retain concise provenance. Report completed work, failures and untested boundaries without inventing tool output or promising unavailable background execution.

## Task-specific details and resources

- Locate the primary auth, endpoint, and error-handling docs first.
- Extract the implementation-critical fields, not just generic overview text.
- Produce a concrete checklist for coding, testing, and operational rollout.

## References

- [OpenAI API docs](https://platform.openai.com/docs/api-reference)
- [Microsoft Learn](https://learn.microsoft.com/)
- [Jina Reader](https://github.com/jina-ai/reader/blob/main/docs/readme.md)
