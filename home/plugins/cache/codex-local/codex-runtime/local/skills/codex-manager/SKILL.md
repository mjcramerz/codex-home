---
name: codex-manager
description: Work in the codex-manager repository across installer flow, home sync boundaries, hook runtime, runtime pack docs, and plugin wiring.
metadata:
  version: '1.0'
  short-description: Installer, home-sync, hooks, and runtime-pack workflows
  tags:
  - codex-manager
interface:
  display-name: Codex Manager
  short-description: Installer, home-sync, hooks, and runtime-pack workflows
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#2563EB'
  default-prompt: Act as the "Codex Manager" specialist for "Installer, home-sync, hooks, and runtime-pack workflows". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- the task directly targets the codex-manager repository/domain surface
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
- `$CODEX_HOME/plugins/cache/codex-local/codex-runtime/local/skills/codex-manager/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/codex-runtime/local/skills/codex-manager/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/workflows/codex-manager.md`
- `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
- `$CODEX_HOME/docs/workflows/codex-mcp.md`
