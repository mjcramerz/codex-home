---
title: Scoped mobile and wireless lab boundary
status: active
owner: Matthew Cramer
tags:
- skills
- all
- mobile-wireless-defense
- references
- authorized-lab-boundary-md
- authorized-lab-boundary
- user
- security-labs
updated: '2026-02-25'
---
# Scoped mobile and wireless lab boundary

Use this reference before wireless assessment, NetHunter build governance checks,
rooted-device risk validation, or BadUSB resilience drills.

## Mandatory controls
- Require explicit owner acknowledgment with a documented `scope_id`.
- Enforce lab-only execution (`lab_only = true`) and an unexpired change window.
- Restrict operations to allowed device IDs and allowed operation classes.
- Prohibit production SSIDs, third-party devices, and covert USB payload behavior.
- Keep evidence of scope checks, commands, findings, and rollback checks.

## Required scope schema
```json
{
  "scope_id": "MOBILE-2026-0012",
  "owner": "mobile-defense-lab",
  "lab_only": true,
  "allowed_devices": ["pixel9a-lab-01", "usbguard-lab-02"],
  "allowed_operations": [
    "wifi-defense-assessment",
    "nethunter-build-validation",
    "rooted-device-risk-check",
    "badusb-defense-drill"
  ],
  "expires_utc": "2026-12-31T23:59:59Z"
}
```

## Stop conditions
- Device or operation is outside the documented scope.
- Scope window is expired.
- Request implies network access outside scope, payload delivery, or anti-theft bypass.
- Rollback or factory recovery path is unavailable.

## References
- NIST SP 800-124r2: https://csrc.nist.gov/publications/detail/sp/800-124/rev-2/draft
- NIST SP 800-153: https://csrc.nist.gov/publications/detail/sp/800-153/final
- OWASP MASVS: https://mas.owasp.org/MASVS/
