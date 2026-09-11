---
name: atlassian-cloud-implementation
description: Turn Atlassian cloud documentation into auth, workflow, and implementation checklists for Jira and Confluence integrations.
metadata:
  version: '1.0'
  short-description: Atlassian Cloud Implementation
  tags:
  - plugin
  - atlassian
---

# Atlassian Cloud Implementation

## Execute the scoped task

1. Resolve the exact resource, account or repository required by the task. Use a relevant read to obtain missing IDs; do not infer access or authorization from a bundled manifest.

2. Inspect the advertised tool contract or the directly linked reference before choosing an operation. Verify version-sensitive behavior against the provider's primary documentation when necessary.

3. Perform the smallest authorized operation, preserving existing data and unrelated work. Confirm the destination and side effects before writes, uploads, notifications or publication.

4. Check the actual result and retain concise provenance. Report completed work, failures and untested boundaries without inventing tool output or promising unavailable background execution.

## Task-specific details and resources

- Start from primary vendor documentation and current product constraints.
- Separate sourced facts from recommended implementation choices.
- Finish with concrete integration, rollout, or validation guidance.

## References

- [Atlassian cloud docs](https://developer.atlassian.com/cloud/)
- [Atlassian platform docs](https://developer.atlassian.com/platform/)
