---
title: secops-supply-chain reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- secops-supply-chain
- references
- latest-sources-md
- latest-sources
- admin
updated: '2026-02-25'
---
# secops-supply-chain reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Strengthen dependency hygiene: pinning, lockfiles, audits, SBOMs, CI enforcement, and avoiding dangerous install patterns.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Mandatory controls (baseline)
- Recommended CI checks
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/security-controls/local/skills/secops-supply-chain/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/security-controls/local/skills/secops-supply-chain/agents/openai.yaml`

## External references
- [SLSA framework](https://slsa.dev/spec/v1.0/levels) - Supply-chain integrity maturity controls.
- [sigstore documentation](https://docs.sigstore.dev/) - Signing and provenance verification workflows.
- [OpenSSF Scorecard](https://securityscorecards.dev/) - Dependency and repository supply-chain checks.
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) - Secure software development supply-chain controls.

## Proof-of-concept prompts
- Build a minimum viable runbook for `secops-supply-chain` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `secops-supply-chain` before finalizing changes.
