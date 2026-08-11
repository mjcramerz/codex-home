---
name: mcp-integration-audit
description: Audit MCP server coverage, auth behavior, timeout settings, dependency wiring, and plugin/skill binding correctness. Use when the user asks to review MCP integrations, remote server definitions, or tool exposure policies.
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
  default-prompt: Act as the "AUDIT-MCP Integration" specialist for "Audit MCP auth, timeouts, and dependency wiring". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Separate transport validity, auth expectations, and runtime enablement concerns.
2) Confirm which dependencies are shared, role-based, or plugin-specific.
3) Flag any config that would hard-fail startup when secrets are unset.

## Agent orchestration
- Confirm ownership, validation scope, and whether another skill or plugin should be combined before editing.
- Delegate only bounded scouting or independent verification work.

## Validation and testing
- Run the narrowest syntax, parser, or unit checks that prove the change.
- Explicitly call out skipped checks and why they remain out of scope.

## Outputs
- Minimal, reviewable edits aligned to the skill contract.
- Concrete validation commands and residual risks.

## References
- [Model Context Protocol](https://modelcontextprotocol.io/introduction)
- [OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
