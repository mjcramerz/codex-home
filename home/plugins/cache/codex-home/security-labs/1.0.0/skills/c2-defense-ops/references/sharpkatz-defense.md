---
title: SharpKatz defense
status: active
owner: Matthew Cramer
tags:
- skills
- all
- c2-defense-ops
- references
- sharpkatz-defense-md
- sharpkatz-defense
- user
- security-labs
updated: '2026-02-20'
---
# SharpKatz defense

## Objective
Validate controls and detections against Mimikatz-like credential access behavior.

## Defensive checks
- LSASS memory access and process-handle anomalies
- privileged token misuse and suspicious process tree behavior
- credential guard / LSASS protection configuration state
- incident response steps for credential theft signals

## Reference sources
- https://attack.mitre.org/tactics/TA0006/
- https://learn.microsoft.com/defender-xdr/advanced-hunting-lsass
- https://www.cisa.gov/news-events/cybersecurity-advisories
