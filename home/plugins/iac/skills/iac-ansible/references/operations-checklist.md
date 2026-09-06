---
title: Operations checklist for iac-ansible
status: active
owner: Matthew Cramer
tags:
- skills
- all
- iac-ansible
- references
- operations-checklist-md
- operations-checklist
- user
- infra
updated: '2026-02-20'
---
# Operations checklist for iac-ansible

## Objective
Keep iac ansible work deterministic, reversible, and security-aware.

## Pre-change
- Confirm target environment, scope boundaries, and maintenance window.
- Record current state and rollback entry points before applying changes.
- Validate input shape/ranges and expected failure handling.

## Change execution
- Apply one coherent change unit at a time.
- Keep commands explicit (no hidden defaults) and capture evidence.
- Stop on first critical regression and execute rollback immediately.

## Post-change validation
- Verify functional behavior, security controls, and performance guardrails.
- Run negative-path checks for the highest-risk boundary.
- Document residual risk and next actions.
