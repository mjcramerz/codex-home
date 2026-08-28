---
title: Reverse engineering triage
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- reverse-engineering-triage-md
- reverse-engineering-triage
- user
- security-labs
updated: '2026-02-20'
---
# Reverse engineering triage

## Objective
Perform fast triage of suspicious binaries/scripts to support detection and containment.

## Workflow
1) Acquire sample safely (hash, provenance, chain of custody).
2) Run static triage first (strings, headers, imports, packer hints).
3) Decide if deep dynamic analysis is required in isolated sandbox.
4) Map behavior to ATT&CK and update defensive controls.
5) Publish IoCs, detections, and response guidance.

## Guardrails
- Analyze unknown samples in isolated lab environments only.
- Block outbound network during initial dynamic analysis unless explicitly required.
- Preserve original sample hashes and timestamps for evidence integrity.

## Outputs
- Triage verdict: benign/suspicious/malicious/unknown
- Behavior summary and impacted controls
- Detection updates (YARA/SIEM/EDR)
- Recommended containment and eradication actions

## References
- Ghidra project: https://ghidra-sre.org/
- CAPA project: https://github.com/mandiant/capa
- CISA malware analysis resources: https://www.cisa.gov/resources-tools/services/malware-analysis
