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

Consult this reference when reverse-shell detection is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

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
