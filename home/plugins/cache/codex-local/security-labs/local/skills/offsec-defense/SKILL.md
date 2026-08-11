---
name: offsec-defense
description: Run scoped offensive-security simulation and cyber-defense operations. Use
  when requests involve documented-scope port scanning, credential-dumping detection (Mimikatz
  behavior), Pi-hole/Unbound DNS defense, Metasploit lab validation, Wi-Fi security assessment,
  purple-team exercises, and reverse-engineering triage in owned or lab environments.
metadata:
  version: '1.0'
  short-description: Scoped offensive simulation and cyber-defense workflow with strict
    safety controls
  tags:
  - offsec-defense
  - cyber-defense
  - offensive-security
  - purple-team
  - reverse-engineering
interface:
  display-name: OffSec Defense
  short-description: Scoped offensive simulation and cyber-defense workflow with strict
    safety controls
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC3232'
  default-prompt: Act as the "OffSec Defense" specialist for "Scoped offensive simulation
    + cyber-defense workflow with strict safety controls". Deliver focused, deterministic
    results with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions,
    evidence, and residual risks.
---

## Use this skill when
- the request combines offensive validation and defensive controls in a documented environment
- you need one workflow that ties together recon, exploit simulation, detection, and remediation

## Scope boundary (required)
- Only operate against assets the user explicitly owns or has documented permission to test.
- Prefer lab/staging targets; for production, require explicit scope, change window, and rollback.
- Refuse credential theft, persistence, malware delivery, or stealth abuse outside permitted assessments.

## Workflow
1) Confirm documented scope with `scripts/scope_guard.py` (`engagement_id`, owner, `lab_only`, `expires_utc`)
   before any offensive action.
2) Build a target inventory and run bounded port/service discovery.
3) Map findings to ATT&CK techniques and defensive telemetry requirements.
4) Execute controlled simulation tracks:
   - port scanning and service triage
   - credential-dumping detection validation (Mimikatz behavior emulation)
   - DNS defense validation for Pi-hole + Unbound
   - Metasploit module/lab validation without uncontrolled payload deployment
   - Wi-Fi security posture checks in the documented RF boundary
   - reverse-engineering triage for suspicious binaries/scripts
5) Run purple-team reconciliation: coverage gaps, missed alerts, and response timing.
6) Produce a prioritized remediation backlog with verification commands and owners.

## Topic coverage map
- Port scanning: `references/port-scanning-and-service-triage.md`
- Mimikatz detection and credential-access controls: `references/credential-dumping-detection.md`
- Pi-hole + Unbound security operations: `references/dns-defense-pihole-unbound.md`
- Metasploit lab workflow: `references/metasploit-lab-validation.md`
- Wi-Fi assessment boundaries and controls: `references/wifi-assessment-lab.md`
- Purple teaming operations: `references/purple-team-operations.md`
- Reverse engineering triage flow: `references/reverse-engineering-triage.md`

## Companion skills
- `c2-defense-ops` for C2/redirector/reverse-shell/credential-access detection operations.
- `mobile-wireless-defense` for wireless/mobile lab defense and NetHunter governance.

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
- Scope-validated assessment plan tied to documented targets.
- Evidence log: commands, artifacts, detections, and timestamped observations.
- Remediation plan with severity, owner, and re-test criteria.

## References
- `references/engagement-boundary.md`
- `references/port-scanning-and-service-triage.md`
- `references/credential-dumping-detection.md`
- `references/dns-defense-pihole-unbound.md`
- `references/metasploit-lab-validation.md`
- `references/wifi-assessment-lab.md`
- `references/purple-team-operations.md`
- `references/reverse-engineering-triage.md`
- `$CODEX_HOME/docs/workflows/offsec-defense.md`
- `$CODEX_HOME/docs/security/security-labs-index.md`
- `$CODEX_HOME/docs/security/security-labs-repo-catalog.md`
- `$CODEX_HOME/docs/security/security-labs-tool-guides.md`
- `$CODEX_HOME/templates/system/offsec-defense-kit/overview.md`
- `$CODEX_HOME/snippets/bash/security_assessment_guardrails.sh`
