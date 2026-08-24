---
title: Metasploit lab validation
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- metasploit-lab-validation-md
- metasploit-lab-validation
- user
- security-labs
updated: '2026-02-20'
---
# Metasploit lab validation

## Objective
Use Metasploit in controlled labs to validate exploitability assumptions and defense controls.

## Boundaries
- Lab-only unless a documented production change window exists.
- No autonomous payload deployment to unknown targets.
- No persistence, lateral movement, or data exfiltration outside test objectives.

## Workflow
1) Validate documented scope and objective.
2) Reproduce vulnerability preconditions on lab targets.
3) Run controlled module validation with explicit operator review.
4) Validate that detections fire and response playbooks trigger.
5) Capture remediation guidance and re-test after fixes.

## Evidence checklist
- Module name, target, and timestamp
- Expected vs observed behavior
- Detection events and containment actions
- Patch/control status and re-test outcome

## References
- Metasploit docs: https://docs.metasploit.com/
- Rapid7 module guidance: https://www.rapid7.com/db/
