# Kubernetes workflow

Use this guide when you change Kubernetes workloads, manifests, Helm charts or cluster operations. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-kubernetes.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Scope**: namespace, RBAC, resources, secrets.
2. **Validate**: schema check, `kubeconform`/`kubectl apply --dry-run=server`.
3. **Apply**: `kubectl apply` with reviewed manifests.
4. **Verify**: rollout status, readiness, and logs.

## Safety rules

- Always set resource requests/limits.
- Avoid `latest` images.
- Keep secrets out of plain YAML.

## Security checkpoints

- Validate namespace and RBAC boundaries for every applied manifest set.
- Require pinned image references and hardened pod security settings.
- Block privileged or hostPath patterns unless explicitly approved.

## Testing checkpoints

- Run schema and policy checks plus `kubectl apply --dry-run=server`.
- Canary deploy and verify probes, rollout status, and service connectivity.
- Exercise rollback path using previous ReplicaSet or release revision.

## Deployment checkpoints

- Apply in dependency order (CRDs, controllers, then workloads).
- Use progressive rollout gates and pause on SLO or readiness regressions.
- Record applied resources, rollout evidence, and incident notes.

## Multi-agent handoff

- Coordinator provides kube-context, namespace scope, and rollout strategy.
- Executor hands off manifest list, rollout outputs, and observed anomalies.
- Receiver monitors stabilization window and owns follow-up manifest changes.
See also:
- `overview.md`
- `../infra/kubernetes.md`
- `$CODEX_HOME/templates/infra/kubernetes-app-skeleton/`
- `$CODEX_HOME/snippets/kubernetes/deployment.yaml`
- Read the `infra-kubernetes` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
