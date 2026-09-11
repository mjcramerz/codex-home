---
title: Rollback checklist (infra-containers)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- assets
- rollback-checklist-md
- rollback-checklist
- user
- infra
updated: '2026-02-20'
---

# Rollback checklist (infra-containers)

Use this guide when you change Docker, Podman, Compose or container build and runtime definitions. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

- Confirm rollback trigger and decision owner.
- Capture diagnostics before reverting.
- Execute documented rollback command sequence.
- Re-validate service health and critical workflows.
- Record incident notes and follow-up remediation tasks.
