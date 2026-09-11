---
name: mcp-integration-audit
description: Use this skill to audit MCP server coverage, auth behavior, timeout settings,
  dependency wiring, and plugin/skill binding correctness. Use this skill when you
  need to review MCP integrations, remote server definitions, or tool exposure policies.
metadata:
  version: '1.0'
  short-description: Audit MCP auth, timeouts, and dependency wiring
  tags:
  - audit
  - mcp
  - integration
  - auth
interface:
  display-name: AUDIT-MCP Integration
  short-description: Audit MCP auth, timeouts, and dependency wiring
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#F97316'
  default-prompt: Act as the "AUDIT-MCP Integration" specialist for "Audit MCP auth,
    timeouts, and dependency wiring". Deliver focused, deterministic results with
    minimal, reviewable changes and explicit assumptions. Validate untrusted inputs
    and bounded I/O, run the narrowest relevant checks, and report concrete actions,
    evidence, and residual risks.
---

# Mcp Integration Audit

## Workflow

1. Inspect actual server transport, launch arguments, credential channel, timeouts and tool filters. Resolve paths in the active deployment.

2. Discover the advertised tool schema and confirm supported arguments before invocation. Separate installation, connection, authentication and authorization.

3. Check stdin/stdout framing, bounded errors, exit handling and isolation boundaries. Never include credentials or full server responses in ambient context.

4. Use read-only health or capability calls where authorized, and report each integration state without treating a manifest as proof of a working service.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
