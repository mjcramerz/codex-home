---
name: docs-research-workbench
description: Compare official docs and turn findings into engineering decisions.
metadata:
  version: '1.0'
  short-description: Docs Research Workbench
  tags:
  - plugin
  - research
  - docs
---

# Docs Research Workbench

## Execute the scoped task

1. Resolve the exact resource, account or repository required by the task. Use a relevant read to obtain missing IDs; do not infer access or authorization from a bundled manifest.

2. Inspect the advertised tool contract or the directly linked reference before choosing an operation. Verify version-sensitive behavior against the provider's primary documentation when necessary.

3. Perform the smallest authorized operation, preserving existing data and unrelated work. Confirm the destination and side effects before writes, uploads, notifications or publication.

4. Check the actual result and retain concise provenance. Report completed work, failures and untested boundaries without inventing tool output or promising unavailable background execution.

## Task-specific details and resources

- Identify the smallest set of primary sources before searching broadly.
- Separate sourced facts from design recommendations.
- Finish with concrete implementation guidance, not just a source dump.

## References

- [OpenAI MCP](https://platform.openai.com/docs/mcp)
- [Microsoft Learn MCP](https://learn.microsoft.com/en-us/azure/developer/ai/azure-ai-foundry-mcp-server)
- [Jina Reader](https://github.com/jina-ai/reader/blob/main/docs/readme.md)
