# Kubernetes

Use this guide when you change Kubernetes workloads, manifests, Helm charts or cluster operations. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to safe, reproducible Kubernetes deployments.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/infra/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Use namespaces and least-privilege RBAC.
- Set resource requests/limits for all workloads.
- Use readiness/liveness probes.
- Pin image tags and avoid `latest`.

## Manifests

- Keep manifests small and composable (use Kustomize where helpful).
- Avoid storing secrets in plain YAML; use external secret stores.

## Safety

- Prefer `kubectl apply` with review in CI.
- Gate changes via PRs and manifest validation.

See also:
- `overview.md`
- `../workflows/kubernetes.md`
- `$CODEX_HOME/templates/infra/kubernetes-app-skeleton/`
- `$CODEX_HOME/snippets/kubernetes/deployment.yaml`
- `$CODEX_HOME/snippets/kubernetes/service.yaml`
- Read the `infra-kubernetes` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/infra/tooling.md`
- `$CODEX_HOME/index/domains/infra/kubernetes.md`
