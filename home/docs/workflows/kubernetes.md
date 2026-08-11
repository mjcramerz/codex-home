# Kubernetes workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-kubernetes.md` before executing this workflow.
Purpose: validate and apply Kubernetes manifests safely for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: namespace, RBAC, resources, secrets.
2) **Validate**: schema check, `kubeconform`/`kubectl apply --dry-run=server`.
3) **Apply**: `kubectl apply` with reviewed manifests.
4) **Verify**: rollout status, readiness, and logs.

## Safety rules
- Always set resource requests/limits.
- Avoid `latest` images.
- You must keep secrets out of plain YAML.

## Security checkpoints
- You must validate namespace and RBAC boundaries for every applied manifest set.
- You must require pinned image references and hardened pod security settings.
- Block privileged or hostPath patterns unless explicitly approved.

## Testing checkpoints
- You must run schema and policy checks plus `kubectl apply --dry-run=server`.
- Canary deploy and verify probes, rollout status, and service connectivity.
- Exercise rollback path using previous ReplicaSet or release revision.

## Deployment checkpoints
- Apply in dependency order (CRDs, controllers, then workloads).
- You must use progressive rollout gates and pause on SLO or readiness regressions.
- You must record applied resources, rollout evidence, and incident notes.

## Multi-agent handoff
- Coordinator provides kube-context, namespace scope, and rollout strategy.
- Executor hands off manifest list, rollout outputs, and observed anomalies.
- Receiver monitors stabilization window and owns follow-up manifest changes.
See also:
- `overview.md`
- `../infra/kubernetes.md`
- `$CODEX_HOME/templates/infra/kubernetes-app-skeleton/`
- `$CODEX_HOME/snippets/kubernetes/deployment.yaml`
- You must use skill `infra-kubernetes`.
- `$CODEX_HOME/index/pack/workflows.md`
