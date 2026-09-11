---
name: dependency-risk-review
description: Use this skill to review dependency surfaces for upgrade risk, auth coupling,
  supply-chain exposure, and missing pinning or verification steps. Use when the user
  asks for dependency audits, risk summaries, or release hardening reviews.
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
  default-prompt: Act as the "AUDIT-Dependency Risk" specialist for "Audit dependency
    risk, pinning, and supply-chain exposure". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete
    actions, evidence, and residual risks.
---

# Dependency Risk Review

## Workflow

1. Map manifests, lockfiles, transitive dependencies, registries and authentication channels for the affected component.

2. Use primary release/security advisories for the exact versions. Distinguish an advisory match from an actually reachable vulnerable feature.

3. Inspect provenance, install scripts, signatures/checksums and pinning policy. Do not disable security checks or refresh unrelated dependencies.

4. Recommend the smallest compatible update or mitigation and verify with existing targeted checks; report unresolved exposure and rollback constraints.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
