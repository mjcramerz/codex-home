---
name: secops-supply-chain
description: Harden software supply-chain controls through dependency pinning, lockfile discipline,
  SBOM generation, and CI enforcement. Use when the user asks about dependency risk, provenance,
  or package security posture.
metadata:
  version: '1.1'
  short-description: 'Strengthen dependency hygiene: pinning, lockfiles, audits, SBOMs, CI
    enforcement, and avoiding dangerous install patterns'
  tags:
  - supply-chain
  - security
  - dependencies
  - ci
interface:
  display-name: SECOPS-Supply Chain
  short-description: 'Strengthen dependency hygiene: pinning, lockfiles, audits, SBOMs, CI
    enforcement, and avoiding dangerous install patterns'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7732CC'
  default-prompt: 'Act as the "SECOPS-Supply Chain" specialist for "Strengthen dependency
    hygiene: pinning, lockfiles, audits, SBOMs, CI enforcement, and avoiding dangerous install
    patterns". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.'
---

## Use this skill when
- adding or updating dependencies
- creating CI workflows
- building installers or build scripts
- consuming binaries or Docker images
- publishing artifacts/releases

## Workflow
1) Clarify objective, trust boundaries, and success criteria.
2) Inspect current implementation and constraints before editing.
3) Apply minimal, deterministic changes using approved patterns.
4) Validate with the narrowest relevant checks and summarize risks/follow-ups.


## Mandatory controls (baseline)
- Minimize new deps; justify each one.
- Pin versions and commit lockfiles.
- Add audit tooling to CI.
- Avoid remote script execution (`curl|sh`).
- Prefer `npm ci`, pinned Python deps, and `Cargo.lock`.
- Prefer pinned CI actions/plugins in high-assurance environments.
- Pin container base images; avoid `:latest`.
- Verify artifact provenance/signatures where ecosystem tooling supports it.
- Fail closed when lockfiles drift from declared manifests.

## Recommended CI checks
- Node: `npm audit`/`pnpm audit` + dependency review
- Python: `pip-audit` or OSV scan
- Rust: `cargo audit` + `cargo deny`
- Generate SBOM on release builds (Syft/CycloneDX)
- Enforce dependency/update policies via branch protection and required status checks.
- Verify signed releases or provenance attestations before promotion.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- Pinned dependencies with committed lockfiles.
- CI gates for audits and dependency review.
- SBOM/provenance outputs (or explicit gap notes) for release-critical artifacts.

## References
- `$CODEX_HOME/docs/security/supply-chain.md`
- `$CODEX_HOME/docs/security/supply-chain-controls.md`
- `$CODEX_HOME/templates/ci/github-actions/`
