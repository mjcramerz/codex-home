---
title: Risk register for iac-terraform
status: active
owner: Matthew Cramer
tags:
- skills
- all
- iac-terraform
- references
- risk-register-md
- risk-register
- user
- infra
updated: '2026-02-20'
---
# Risk register for iac-terraform

| Risk area | Example failure mode | Preventive control | Detection signal | Recovery action |
| --- | --- | --- | --- | --- |
| Input validation | Invalid values trigger destructive behavior | Validate format/range before execution | Command pre-check fails | Block apply and request corrected input |
| Security | Excessive privileges or unsafe mounts/network | Least-privilege defaults and explicit exceptions | Security lint/review flags | Revert to hardened baseline |
| Availability | Service disruption during rollout | Canary-first and bounded rollout steps | Health checks fail | Roll back to prior known-good state |
| Performance | Latency/throughput regressions | Baseline metrics and guardrail thresholds | Metric deltas exceed threshold | Restore previous configuration |
| Recoverability | Missing rollback artifacts | Pre-stage rollback commands and snapshots | Rollback command unavailable | Rebuild from last validated backup |
