---
name: gitops
description: Plan GitOps delivery flows with protected refs, environment promotion order, and declarative desired-state review boundaries. Use when the user asks about Git-driven promotion, environment repos, or reconciliation-safe delivery contracts.
metadata:
  version: '1.0'
  short-description: Protected-ref promotion and desired-state delivery discipline
  tags:
  - gitops
  - gitlab
  - delivery
  - promotion
interface:
  display-name: GitOps
  short-description: Protected-ref promotion and desired-state delivery discipline
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#0F766E'
  default-prompt: Act as the "GitOps" specialist for "Protected-ref promotion and desired-state delivery discipline". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing desired-state repository promotion and branch protection
- checking environment drift controls, reconciliation order, or rollback notes
- aligning CI mutation steps with Git-driven delivery expectations

## Workflow
1) Confirm the source-of-truth repo, promotion branches, and reconciliation controller boundaries first.
2) Keep release mutations deterministic and minimize direct edits on deployed branches.
3) Separate desired-state generation from apply/reconcile triggers so rollback stays clear.
4) Validate branch, tag, and environment promotion order before widening rollout.

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
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/local/skills/gitops/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/gitlab/local/skills/gitops/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/gitops.md
- $CODEX_HOME/docs/infra/gitops.md
- $CODEX_HOME/index/domains/infra/gitops.md
