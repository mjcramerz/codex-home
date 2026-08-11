---
title: Runtime security matrix
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- runtime-security-matrix-md
- runtime-security-matrix
- user
- infra
updated: '2026-02-20'
---
# Runtime security matrix

## Objective
Map container runtime choices to privilege and network exposure risk so deployment reviews stay deterministic.

## Matrix
| Runtime mode | Primary use case | Risk profile | Required controls | Verify with |
| --- | --- | --- | --- | --- |
| Docker rootless | Developer workstation and CI sandboxes | Low-to-medium | Non-root container user, explicit published ports, pinned image digest | `docker info`, `id`, `docker inspect` |
| Docker rootful | Host-level services needing kernel integrations | Medium-to-high | Explicit exception approval, capability minimization, audited mount list | `docker inspect`, service smoke checks |
| Podman rootless | Daemonless workflows and constrained hosts | Low-to-medium | `userns=keep-id`, read-only rootfs where possible, cgroup limits | `podman info`, `podman inspect` |

## Gate checklist
- Confirm why rootless is not feasible before allowing rootful runtime.
- Record required capabilities and why each is needed.
- Ensure host path mounts are least-privilege and writable only when needed.
- Require rollback target (previous digest/tag) before changing production images.
