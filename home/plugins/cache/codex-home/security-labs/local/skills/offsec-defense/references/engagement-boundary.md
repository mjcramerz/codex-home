---
title: Scoped security engagement boundary
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- authorized-engagement-md
- authorized-engagement
- user
- security-labs
updated: '2026-02-20'
---
# Scoped security engagement boundary

Use this reference before any offensive or dual-use operation.

## Mandatory controls
- Require explicit user authorization and documented target ownership.
- Keep operations scoped to allowed networks and systems only.
- Prefer lab or staging environments for exploit simulation.
- Require a documented scope identifier for offensive tracks.
- Require a named owner, `lab_only = true`, and a non-expired `expires_utc` window.
- Keep an evidence trail: timestamp, operator, target, command class, and outcome.

## Required scope file schema
```json
{
  "scope_id": "SEC-2026-0001",
  "owner": "security-lab-team",
  "lab_only": true,
  "allowed_networks": ["10.10.0.0/24", "192.168.56.0/24"],
  "allowed_operations": [
    "port-scan",
    "credential-detection-test",
    "dns-defense-validation",
    "metasploit-lab-validation",
    "wifi-security-assessment",
    "purple-team-replay",
    "reverse-engineering-triage"
  ],
  "expires_utc": "2026-12-31T23:59:59Z"
}
```

## Stop conditions
- Target is outside the documented scope.
- Scope is expired or `lab_only` is false.
- User asks for stealth abuse, persistence, ransomware behavior, or credential theft.
- No rollback or containment path is available.
- Production risk is unclear or change window is missing.

## References
- MITRE ATT&CK: https://attack.mitre.org/
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-115: https://csrc.nist.gov/publications/detail/sp/800-115/final
