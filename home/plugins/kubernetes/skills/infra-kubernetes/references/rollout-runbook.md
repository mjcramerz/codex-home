---
title: Rollout and rollback runbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-kubernetes
- references
- rollout-runbook-md
- rollout-runbook
- user
- infra
updated: '2026-02-20'
---

# Rollout and rollback runbook

Consult this reference when rollout and rollback runbook is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Pre-rollout

```bash
kubectl apply --dry-run=server -f k8s/
kubectl diff -f k8s/
```

## Rollout

```bash
kubectl apply -f k8s/
kubectl rollout status deploy/<name> -n <namespace> --timeout=5m
```

## Rollback triggers

- Probe failures above SLO threshold
- Error budget burn rate exceeds agreed guardrail
- Critical dependency connectivity loss

## Rollback commands

```bash
kubectl rollout undo deploy/<name> -n <namespace>
kubectl get events -n <namespace> --sort-by=.lastTimestamp
```
