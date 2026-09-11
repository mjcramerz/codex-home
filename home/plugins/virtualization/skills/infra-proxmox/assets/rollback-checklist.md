---
title: Rollback checklist (infra-proxmox)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-proxmox
- assets
- rollback-checklist-md
- rollback-checklist
- user
- infra
updated: '2026-02-20'
---

# Rollback checklist (infra-proxmox)

Use this guide when you change Debian packaging, APT configuration, installation or host integration. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

- Confirm rollback trigger and decision owner.
- Capture diagnostics before reverting.
- Execute documented rollback command sequence.
- Re-validate service health and critical workflows.
- Record incident notes and follow-up remediation tasks.
