---
name: debian-preseed
description: Plan and review Debian preseed repositories with class manifests, destructive-storage safeguards, and staged installer hooks. Use when the user asks about unattended Debian installs, preseed class selection, or installer delivery contracts.
metadata:
  version: '1.0'
  short-description: Debian unattended install contracts and class-driven provisioning
  tags:
  - debian
  - preseed
  - installer
  - unattended
interface:
  display-name: Debian Preseed
  short-description: Debian unattended install contracts and class-driven provisioning
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3265CC'
  default-prompt: Act as the "Debian Preseed" specialist for "Debian unattended install contracts and class-driven provisioning". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing split preseed trees, class selectors, or late-command behavior
- mapping kernel cmdline answers to staged installer/runtime actions
- checking destructive storage, network, or addon-class changes before rollout

## Workflow
1) Confirm the class manifest, profile family, and destructive storage targets first.
2) Keep installer answers, class fragments, and target-side runtime scripts separated by responsibility.
3) Prefer repo-relative include paths and staged helper scripts over long inline shell payloads.
4) Validate happy-path and failure-path installs with the narrowest available smoke tests before widening scope.

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
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/debian-preseed/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/debian-preseed/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/debian-preseed.md
- $CODEX_HOME/docs/virtualization/debian-preseed.md
- $CODEX_HOME/index/domains/system/debian-preseed.md
