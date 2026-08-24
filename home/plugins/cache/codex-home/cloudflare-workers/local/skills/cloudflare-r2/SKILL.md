---
name: cloudflare-r2
description: Operate Cloudflare R2-backed publication and artifact delivery paths with explicit bucket, prefix, credential, and immutability rules. Use when the user asks about R2 storage behavior, signed access, or artifact publication through Cloudflare.
metadata:
  version: '1.0'
  short-description: R2 bucket, prefix, and publication-front-end contracts
  tags:
  - cloudflare
  - r2
  - storage
  - delivery
interface:
  display-name: Cloudflare R2
  short-description: R2 bucket, prefix, and publication-front-end contracts
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#F97316'
  default-prompt: Act as the "Cloudflare R2" specialist for "R2 bucket, prefix, and publication-front-end contracts". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing R2 bucket/prefix naming, retention, or access policy
- checking how package or build artifacts are exposed through a Cloudflare front-end
- aligning secrets, publication jobs, and runtime reads across delivery systems

## Workflow
1) Confirm the bucket, prefix, and access model before editing publication code or CI wiring.
2) Keep write credentials, signing secrets, and endpoint hostnames out of tracked artifacts.
3) Prefer immutable object keys and deterministic metadata over in-place replacement.
4) Validate both upload and readback contracts with the smallest artifact set that proves the change.

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
- `$CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare-r2/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare-r2/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/cloudflare-r2.md
- $CODEX_HOME/docs/infra/cloudflare-r2.md
- $CODEX_HOME/index/domains/infra/cloudflare-r2.md
