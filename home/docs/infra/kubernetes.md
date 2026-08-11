# Kubernetes
Purpose: tell the Codex coding agent how to use `docs/infra/kubernetes.md` as a runtime-pack surface and when to stop browsing.
Guidance for safe, reproducible Kubernetes deployments.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/infra/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must use namespaces and least-privilege RBAC.
- Set resource requests/limits for all workloads.
- You must use readiness/liveness probes.
- Pin image tags and avoid `latest`.

## Manifests
- You must keep manifests small and composable (use Kustomize where helpful).
- Avoid storing secrets in plain YAML; use external secret stores.

## Safety
- You must prefer `kubectl apply` with review in CI.
- Gate changes via PRs and manifest validation.

See also:
- `overview.md`
- `../workflows/kubernetes.md`
- `$CODEX_HOME/templates/infra/kubernetes-app-skeleton/`
- `$CODEX_HOME/snippets/kubernetes/deployment.yaml`
- `$CODEX_HOME/snippets/kubernetes/service.yaml`
- You must use skill infra-kubernetes.
- `$CODEX_HOME/index/domains/infra/tooling.md`
- `$CODEX_HOME/index/domains/infra/kubernetes.md`
