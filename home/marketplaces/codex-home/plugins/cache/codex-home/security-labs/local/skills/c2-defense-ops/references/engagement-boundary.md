---
title: Scoped C2 defense engagement boundary
status: active
owner: Matthew Cramer
tags:
- skills
- all
- c2-defense-ops
- references
- authorized-engagement-md
- authorized-engagement
- user
- security-labs
updated: '2026-02-25'
---
# Scoped C2 defense engagement boundary

Use this reference before C2 simulation, redirector replay, reverse-shell telemetry checks,
or credential-access detection validation.

## Mandatory controls
- Require explicit owner acknowledgment and a documented `scope_id`.
- Restrict execution to documented lab windows (`lab_only = true` + unexpired `expires_utc`).
- Allow only declared operation classes from the documented operation list.
- Require allowed target labels; deny unlabeled or ad-hoc targets.
- Stop immediately on scope drift and capture evidence for audit.

## Required scope schema
```json
{
  "scope_id": "C2-2026-0007",
  "owner": "soc-purple-team",
  "lab_only": true,
  "allowed_target_labels": ["lab-segment-a", "redirector-stack-01"],
  "allowed_operations": [
    "c2-detection-replay",
    "redirector-validation",
    "reverse-shell-detection",
    "credential-access-detection"
  ],
  "expires_utc": "2026-12-31T23:59:59Z"
}
```

## Stop conditions
- Scope file is missing required keys or has unsupported values.
- Requested operation or target label is not listed in scope.
- Scope window is expired.
- Requested action drifts into stealth persistence, lateral movement outside scope, or payload abuse.

## References
- MITRE ATT&CK command and control: https://attack.mitre.org/tactics/TA0011/
- NIST SP 800-61r2: https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
- CISA Cobalt Strike advisory: https://www.cisa.gov/resources-tools/resources/joint-cybersecurity-advisory-detection-and-mitigation-cobalt-strike
