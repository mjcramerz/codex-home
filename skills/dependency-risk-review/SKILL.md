---
name: dependency-risk-review
description: Review dependency surfaces for upgrade risk, auth coupling, supply-chain exposure, and missing pinning or verification steps. Use when the user asks for dependency audits, risk summaries, or release hardening reviews.
metadata:
  version: '1.0'
  short-description: Audit dependency risk, pinning, and supply-chain exposure
  tags:
  - audit
  - dependencies
  - supply-chain
  - risk
interface:
  display-name: AUDIT-Dependency Risk
  short-description: Audit dependency risk, pinning, and supply-chain exposure
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#EF4444'
  default-prompt: Act as the "AUDIT-Dependency Risk" specialist for "Audit dependency risk, pinning, and supply-chain exposure". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Inventory the dependency surface before ranking risks.
2) Separate direct runtime dependencies from tooling-only or generation-only dependencies.
3) Tie each recommendation to concrete verification or pinning changes.

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
- [SLSA](https://slsa.dev/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final)
