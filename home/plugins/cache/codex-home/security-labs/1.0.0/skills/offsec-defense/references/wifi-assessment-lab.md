---
title: Wi-Fi security assessment (documented RF boundaries)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- wifi-assessment-lab-md
- wifi-assessment-lab
- user
- security-labs
updated: '2026-02-20'
---
# Wi-Fi security assessment (documented RF boundaries)

## Objective
Assess wireless posture and detection readiness in documented test areas.

## Scope controls
- Use only organization-owned APs, clients, and frequencies.
- Document physical boundary and test window.
- Coordinate with operations to avoid production disruption.

## Assessment focus
- Encryption posture (WPA2/WPA3, transition mode risk).
- Weak management/configuration controls.
- Rogue AP detection and containment workflow.
- Monitoring coverage for anomalous auth/deauth activity.

## Defensive outcomes
- Harden AP configurations and disable insecure compatibility modes.
- Improve NAC policy for unknown wireless clients.
- Add alert rules for suspicious wireless events.
- Practice IR runbook for rogue AP and credential abuse scenarios.

## References
- NIST wireless security guidance: https://csrc.nist.gov/publications/detail/sp/800-153/final
- Wi-Fi Alliance security: https://www.wi-fi.org/discover-wi-fi/security
