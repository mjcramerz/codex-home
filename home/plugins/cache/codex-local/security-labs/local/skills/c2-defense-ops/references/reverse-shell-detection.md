---
title: Reverse-shell detection
status: active
owner: Matthew Cramer
tags:
- skills
- all
- c2-defense-ops
- references
- reverse-shell-detection-md
- reverse-shell-detection
- user
- security-labs
updated: '2026-02-20'
---
# Reverse-shell detection

## Objective
Detect suspicious outbound command channels and isolate affected hosts quickly.

## Defensive checks
- unusual long-lived outbound sessions to untrusted endpoints
- shell process lineage connected to sockets
- encrypted channels on unexpected ports/processes
- repeated reconnect patterns after process restart

## Reference sources
- https://attack.mitre.org/techniques/T1059/
- https://attack.mitre.org/techniques/T1071/
- https://www.cisa.gov/resources-tools/resources/secure-by-design-alert-series
