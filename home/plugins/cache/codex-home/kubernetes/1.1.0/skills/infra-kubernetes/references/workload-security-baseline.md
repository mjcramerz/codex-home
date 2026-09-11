---
title: Workload security baseline
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-kubernetes
- references
- workload-security-baseline-md
- workload-security-baseline
- user
- infra
updated: '2026-02-20'
---

# Workload security baseline

Consult this reference when workload security baseline is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Required pod security controls

- `runAsNonRoot: true`
- `allowPrivilegeEscalation: false`
- `readOnlyRootFilesystem: true` where feasible
- `seccompProfile.type: RuntimeDefault`
- Drop all capabilities by default and add back only documented exceptions

## Manifest review checklist

- Confirm namespace and ownership labels are explicit.
- Require resource requests/limits on every container.
- Ensure readiness and liveness probes are present and bounded.
- Validate service account and RBAC least privilege.
- Apply default deny network policies when namespace is multi-tenant.
