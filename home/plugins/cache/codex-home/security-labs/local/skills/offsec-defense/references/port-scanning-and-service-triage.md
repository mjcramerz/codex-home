---
title: Port scanning and service triage (authorized scope)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- port-scanning-and-service-triage-md
- port-scanning-and-service-triage
- user
- security-labs
updated: '2026-02-20'
---
# Port scanning and service triage (authorized scope)

## Objective
Discover exposed services in documented ranges, then prioritize remediation.

## Procedure
1) Validate target scope with `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/offsec-defense/scripts/scope_guard.py`.
2) Run bounded discovery (time-limited scans, explicit targets).
3) Normalize findings by service, version, and exposure path.
4) Correlate with known CVEs and patch levels.
5) Open remediation actions with owner + due date.

## Defensive checks
- Enforce scan-rate and timeout limits to avoid service disruption.
- Capture false positives with manual validation on critical hosts.
- Compare results with CMDB/inventory to detect shadow services.
- Re-scan after patching to confirm closure.

## Data to capture
- target, scan timestamp, scanner version
- open ports, service banners, TLS details
- inferred risk score and business impact

## References
- Nmap reference guide: https://nmap.org/book/man.html
- CIS Controls v8: https://www.cisecurity.org/controls/v8
