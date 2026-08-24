---
name: infra-kubernetes
description: Create and validate Kubernetes manifests, workload configs, and cluster operation
  patterns with secure defaults. Use when the user asks for Kubernetes YAML, deployment troubleshooting,
  or k8s hardening.
metadata:
  version: '1.0'
  short-description: Build and validate Kubernetes manifests with safe defaults
  tags:
  - kubernetes
  - k8s
  - infra
  - security
interface:
  display-name: INFRA-Kubernetes
  short-description: Build and validate Kubernetes manifests with safe defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC63'
  default-prompt: Act as the "INFRA-Kubernetes" specialist for "Build and validate Kubernetes
    manifests with safe defaults". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- creating or reviewing Kubernetes manifests
- planning deployments and rollouts

## Workflow
1) Validate manifests and schemas.
2) Ensure resource limits and probes are set.
3) Apply with review and verify rollout status.

## Checkpoint gates
- Manifest gate: ensure namespace, labels, resource requests/limits, probes, and disruption settings match workload SLOs.
- Security gate: require non-root runtime defaults (`runAsNonRoot`, dropped capabilities, seccomp profile), enforce Pod Security Admission targets (Baseline/Restricted) unless justified.
- Pre-apply gate: run dry-run and diff against target cluster before any change window.
- Rollout gate: use explicit rollout strategy (`maxUnavailable`, `maxSurge`, canary namespace/selector) and define rollback trigger.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Schema validation: run local render + validation (`kubectl kustomize`, `kubectl apply --dry-run=client -f ...`) and policy checks used by the target cluster.
- Cluster validation: run server-side validation and diff (`kubectl apply --dry-run=server -f ...`, `kubectl diff -f ...`).
- Deployment validation: apply in scoped order, then verify with `kubectl rollout status`, `kubectl get events`, and targeted readiness checks.
- Service validation: confirm endpoint/service reachability and check logs for startup/probe failures before broad rollout.
- Rollback readiness: provide tested undo commands (`kubectl rollout undo` or previous manifest apply path).

## Outputs
- Manifest bundle with environment overlays and explicit security/resource assumptions.
- Rollout plan with dry-run, apply, verify, and rollback commands tied to namespace/context.
- Validation evidence including rollout status, key events/log findings, and unresolved risks.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/scripts/skill_helper.py`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/references/rollout-runbook.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/references/workload-security-baseline.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/assets/deployment-baseline.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/assets/networkpolicy-default-deny.yaml`

## References
- `$CODEX_HOME/docs/workflows/kubernetes.md`
- `$CODEX_HOME/docs/infra/kubernetes.md`
- `$CODEX_HOME/templates/infra/kubernetes-app-skeleton/`
- `$CODEX_HOME/snippets/kubernetes/deployment.yaml`
