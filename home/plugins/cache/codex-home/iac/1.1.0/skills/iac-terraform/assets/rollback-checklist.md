---
title: Rollback checklist (iac-terraform)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- iac-terraform
- assets
- rollback-checklist-md
- rollback-checklist
- user
- infra
updated: '2026-02-20'
---

# Rollback checklist (iac-terraform)

Use this guide when you change Terraform modules, providers, state or infrastructure plans. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

- Confirm rollback trigger and decision owner.
- Capture diagnostics before reverting.
- Execute documented rollback command sequence.
- Re-validate service health and critical workflows.
- Record incident notes and follow-up remediation tasks.
