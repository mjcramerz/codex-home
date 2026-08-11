# Offsec defense reference
Purpose: tell the Codex coding agent how to use `docs/security/offsec-defense.md` as a runtime-pack surface and when to stop browsing.

This reference supports reusable offsec-defense and cyber-defense work with explicit scope, evidence, and rollback boundaries.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Intent
- Combine scoped offensive simulation with practical defensive outcomes.
- You must keep assessments bounded, evidence-backed, and reversible.
- Prioritize risk reduction over exploit novelty.

## Coverage domains
- Port scanning and service exposure triage.
- Credential-access detection validation (Mimikatz behavior).
- DNS defense operations (Pi-hole + Unbound).
- Metasploit lab validation for exploitability assumptions.
- Wi-Fi security posture assessment in controlled boundaries.
- Purple-team detection and response rehearsal.
- Reverse-engineering triage for suspicious binaries and scripts.

## Control baseline
- Documented scope manifest before offensive actions.
- Deterministic commands with bounded retries/timeouts.
- Artifact retention and redaction policy for sensitive evidence.
- Containment-first response whenever detection indicates active risk.

## Operational outputs
- Scope validation record
- Findings backlog with severity/owner/due date
- Detection gap register with mapped ATT&CK techniques
- Re-test report showing closure status

See also:
- `nethunter-pixel9a.md`
- `../workflows/offsec-defense.md`
- `security-labs-index.md`
- `security-labs-repo-catalog.md`
- `security-labs-tool-guides.md`
- `$CODEX_HOME/plans/workflows/workflow-offsec-defense.md`
- You must use skill offsec-defense.
