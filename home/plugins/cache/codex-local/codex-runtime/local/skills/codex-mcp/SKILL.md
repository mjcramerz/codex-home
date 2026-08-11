---
name: codex-mcp
description: Work in the codex-mcp repository across config rendering, runtime state, SSH material, Podman launch behavior, and verification flows.
metadata:
  version: '1.0'
  short-description: Podman-backed MCP stack rendering and validation
  tags:
  - codex-mcp
interface:
  display-name: Codex MCP
  short-description: Podman-backed MCP stack rendering and validation
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#0F766E'
  default-prompt: Act as the "Codex MCP" specialist for "Podman-backed MCP stack rendering and validation". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- the task directly targets the codex-mcp repository/domain surface
- repo contracts, CI, or runtime behavior must stay aligned with the active source tree
- validation evidence is needed for a cross-file operational change

## Workflow
1) Read the repo anchors in `references/latest-sources.md`.
2) Confirm the smallest affected surface before editing.
3) Keep secrets, runtime-only state, and generated artifacts out of source-controlled changes.
4) Run the narrowest syntax, unit, or contract checks that prove the change.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Reparse structured config after mutation.
- Run repo-local lint/test/build commands when the touched surface ships them.
- Record residual gaps when external credentials or infrastructure are required for deeper verification.

## Outputs
- Reviewable changes with explicit validation evidence.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/codex-runtime/local/skills/codex-mcp/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/codex-runtime/local/skills/codex-mcp/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/workflows/codex-manager.md`
- `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
- `$CODEX_HOME/docs/workflows/codex-mcp.md`
