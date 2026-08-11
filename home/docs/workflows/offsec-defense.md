# Offsec defense workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-offsec-defense.md` before executing this workflow.
Purpose: run scoped offensive simulation with cyber-defense outcomes for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Workflow steps
1) Validate documented scope and target ownership.
2) Build a deterministic assessment plan (targets, windows, guardrails, rollback).
3) Run bounded offensive simulation tracks in the documented scope:
   - port/service discovery
   - credential-access detection tests (Mimikatz behavior simulation)
   - Metasploit lab validation
   - Wi-Fi security assessment
4) Run defense tracks in parallel:
   - Pi-hole/Unbound DNS hardening and telemetry validation
   - purple-team detection and response coverage review
   - reverse-engineering triage for suspicious artifacts
5) Produce evidence, prioritized remediation backlog, and re-test plan.

## Required artifacts
- Scope file with scope ID and allowed operation classes.
- Timestamped evidence log (commands, outputs, detection events).
- Risk-ranked findings with owners and retest criteria.

## Tool guidance map
- See `../security/security-labs-tool-guides.md` for defensive command baselines.
- See `../security/security-labs-repo-catalog.md` for authoritative source mapping.
- See `../security/security-labs-index.md` for security-operations navigation.

## Security checkpoints
- You must confirm operations are limited to the documented targets and change windows.
- Reject stealth abuse, persistence, credential theft, and uncontrolled payload use.
- Ensure secrets, tokens, and captured data are handled with least privilege and retention limits.

## Testing checkpoints
- You must validate each track with deterministic commands and explicit timeout/retry bounds.
- Include negative tests for missed detections and broken controls.
- You must re-run targeted tests after each remediation item and record pass/fail evidence.

## Deployment checkpoints
- You must use change windows and rollback notes for production-adjacent validation.
- You must require owner acknowledgment before applying defensive control changes.
- You must confirm post-change monitoring for regressions and false positives.

## Multi-agent handoff
- Coordinator assigns one owner for scope validation and one owner for evidence quality.
- Executors report exact targets, commands, and outcomes for each simulation track.
- Final reviewer reconciles findings, coverage gaps, and remediation priorities before closure.

See also:
- `nethunter-pixel9a.md`
- `../security/offsec-defense.md`
- `../security/security-labs-index.md`
- `../security/security-labs-repo-catalog.md`
- `../security/security-labs-tool-guides.md`
- `$CODEX_HOME/templates/system/offsec-defense-kit/overview.md`
- `$CODEX_HOME/snippets/bash/security_assessment_guardrails.sh`
- You must use skill `offsec-defense`.
