---
title: Secops Supply Chain Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- secops-supply-chain
- rules
- rules-md
- admin
updated: '2026-02-20'
---

# Secops Supply Chain Rules

Apply the following secops supply chain rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/security-controls/skills/secops-supply-chain/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/security-controls/skills/secops-supply-chain/scripts/`.
- Use references in `$CODEX_HOME/plugins/security-controls/skills/secops-supply-chain/references/` for factual guidance.
- Require pinned versions, committed lockfiles, and explicit dependency-change rationale.
- Avoid unsafe install patterns (`curl|sh`, floating tags, unsigned binaries) by default.
- Capture audit/SBOM/provenance evidence (or explicit gap notes) for release-critical changes.
