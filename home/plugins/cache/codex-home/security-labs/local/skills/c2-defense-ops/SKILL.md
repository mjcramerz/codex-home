---
name: c2-defense-ops
description: Run scoped C2 simulation defense operations for Cobalt Strike-like traffic,
  redirector behavior, reverse-shell telemetry, and SharpKatz-style credential access
  detection. Use for detection engineering, controlled purple-team replay, and containment
  validation in documented scope.
metadata:
  version: '1.0'
  short-description: Scoped C2 and credential-access defense operations with strict scope
    controls
  tags:
  - c2-defense-ops
  - c2
  - cobalt-strike
  - reverse-shell
  - sharpkatz
interface:
  display-name: C2 Defense Ops
  short-description: Scoped C2 and credential-access defense operations with strict scope
    controls
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC5A32'
  default-prompt: Act as the "C2 Defense Ops" specialist for "Scoped C2 and credential-access
    defense operations with strict scope controls". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs
    and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

## Use this skill when
- the request targets C2/persistence detection operations
- the objective is defensive simulation, telemetry validation, or containment readiness
- the scope includes Cobalt Strike patterns, redirectors, reverse shells, or SharpKatz behavior

## Scope boundary (required)
- Require explicit documented scope for live targets or replay activity.
- No stealth abuse, persistence enablement, or credential theft.
- Restrict simulation to sanctioned infrastructure and documented windows.

## Workflow
1) Validate scope and operation class with `scripts/c2_scope_guard.py` using
   `references/engagement-boundary.md`.
2) Build telemetry baseline (network, process, authentication, endpoint controls).
3) Execute controlled replay and detection checks for:
   - C2 callback patterns and redirector behavior
   - reverse-shell egress signatures
   - SharpKatz-like credential-access attempts
4) Validate containment and incident-response runbooks.
5) Publish detection gaps, remediation owners, and re-test criteria.

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
- Scope-validated C2 defense assessment.
- Detection and containment coverage matrix.
- Prioritized defensive remediation backlog with evidence.

## References
- `references/engagement-boundary.md`
- `references/cobalt-strike-defense.md`
- `references/reverse-shell-detection.md`
- `references/sharpkatz-defense.md`
- `references/redwarden-detection.md`
- `references/latest-sources.md`
- `$CODEX_HOME/docs/security/security-labs-tool-guides.md`
- `$CODEX_HOME/docs/security/security-labs-repo-catalog.md`
