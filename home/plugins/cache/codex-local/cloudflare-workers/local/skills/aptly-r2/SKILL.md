---
name: aptly-r2
description: Work in Cloudflare R2-backed Aptly publication flows across bucket or prefix layout, Worker routing, signed assets, and shared GitLab delivery templates.
metadata:
  version: '1.0'
  short-description: Aptly publication through R2 and Cloudflare Worker delivery
  tags:
  - aptly-r2
interface:
  display-name: Aptly R2
  short-description: Aptly publication through R2 and Cloudflare Worker delivery
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#0EA5E9'
  default-prompt: Act as the "Aptly R2" specialist for "Aptly publication through R2 and Cloudflare Worker delivery". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- the task directly targets an Aptly-to-R2 publication surface
- repo contracts, CI, or runtime behavior must stay aligned with the active source tree
- validation evidence is needed for a cross-file operational change

## Workflow
1) Read the repo anchors in `references/latest-sources.md`.
2) Confirm the smallest affected surface before editing.
3) Keep secrets, runtime-only state, and generated artifacts out of source-controlled changes.
4) Run the narrowest syntax, unit, or contract checks that prove the change across both publication and readback paths.

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
- `$CODEX_HOME/plugins/cache/codex-local/cloudflare-workers/local/skills/aptly-r2/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/cloudflare-workers/local/skills/aptly-r2/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/infra/aptly.md`
- `$CODEX_HOME/docs/infra/cloudflare-r2.md`
- `$CODEX_HOME/docs/workflows/codex-manager.md`
- `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
- `$CODEX_HOME/docs/workflows/codex-mcp.md`
