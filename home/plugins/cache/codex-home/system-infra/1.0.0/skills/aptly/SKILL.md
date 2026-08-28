---
name: aptly
description: Manage Aptly repositories with deterministic snapshot promotion, signing, cleanup, and publication contracts. Use when the user asks about package publication channels, retention, or managed Aptly service behavior.
metadata:
  version: '1.0'
  short-description: Signed channel publication, snapshot retention, and queue safety
  tags:
  - aptly
  - debian
  - packages
  - signing
interface:
  display-name: Aptly
  short-description: Signed channel publication, snapshot retention, and queue safety
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#0EA5E9'
  default-prompt: Act as the "Aptly" specialist for "Signed channel publication, snapshot retention, and queue safety". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing Aptly channel definitions, snapshot retention, or signed publication policy
- checking queue/state directory separation and non-interactive publish helpers
- aligning package publication behavior with GitLab delivery jobs or Cloudflare front-ends

## Workflow
1) Confirm channel names, publish endpoints, and signing material boundaries first.
2) Keep state, queue, cache, and secrets directories explicit and non-overlapping.
3) Prefer append-only snapshot publication and deterministic cleanup thresholds over ad-hoc rewrites.
4) Validate with focused functional checks for publish helpers, retention, and path ownership before rollout.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Reparse structured config after mutation.
- Run repo-local lint/test/build commands when the touched surface ships them.
- Record residual gaps when external credentials or infrastructure are required for deeper verification.

## Outputs
- Reviewable changes with explicit validation evidence.
- A concise contract summary, the files or jobs touched, and the remaining rollout risks.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/aptly/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/aptly/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/aptly.md
- $CODEX_HOME/docs/infra/aptly.md
- $CODEX_HOME/index/domains/infra/aptly.md
