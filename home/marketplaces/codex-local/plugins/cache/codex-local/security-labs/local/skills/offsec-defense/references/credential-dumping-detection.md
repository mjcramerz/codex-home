---
title: Credential dumping detection (Mimikatz behavior)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- credential-dumping-detection-md
- credential-dumping-detection
- user
- security-labs
updated: '2026-02-20'
---
# Credential dumping detection (Mimikatz behavior)

## Objective
Validate detection and response for credential-access behavior without unauthorized credential theft.

## Scope
- Focus on ATT&CK technique coverage, telemetry quality, and containment speed.
- Use documented test hosts and sanctioned simulations only.

## Detection priorities
- LSASS memory access anomalies.
- Suspicious handle access to credential-protected processes.
- Command-line/process lineage associated with known credential dumping patterns.
- Privilege escalation and token abuse signals that precede dumping attempts.

## Blue-team validation
1) Confirm endpoint telemetry includes process, module, and handle events.
2) Confirm SIEM rules map to ATT&CK credential-access techniques.
3) Execute a controlled simulation in a lab host.
4) Measure alert latency, triage quality, and containment action time.
5) Record missed detections and close gaps with rule + hardening updates.

## Hardening controls
- Enable LSASS protection and credential guard where available.
- Restrict debug privileges and administrative token sprawl.
- Harden PowerShell and script execution policies.
- Enforce endpoint isolation runbooks for confirmed credential-access events.

## References
- MITRE ATT&CK credential access: https://attack.mitre.org/tactics/TA0006/
- Microsoft Defender threat analytics: https://learn.microsoft.com/defender-xdr/threat-analytics
