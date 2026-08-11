---
name: installer-regression-audit
description: Review install, home-sync, admin, upgrade, and cleanup flows for regressions, permission boundaries, and preserved-state drift. Use when the user asks for installer audits or rollout safety reviews.
metadata:
  version: '1.0'
  short-description: Audit installer flows for regressions and permission drift
  tags:
  - audit
  - installer
  - regression
  - permissions
interface:
  display-name: AUDIT-Installer Regression
  short-description: Audit installer flows for regressions and permission drift
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#2563EB'
  default-prompt: Act as the "AUDIT-Installer Regression" specialist for "Audit installer flows for regressions and permission drift". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Trace install, home, admin, and upgrade paths separately.
2) Verify runtime-only state never syncs back into source, and check preserved roots, backups, and destructive boundaries explicitly.
3) Tie each concern to a narrow proof command such as py_compile, preflight, or verify.

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
- [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final)
- [The Twelve-Factor App](https://12factor.net/)
