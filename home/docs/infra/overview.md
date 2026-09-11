# Infrastructure overview

Use this guide when the task concerns infrastructure. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Scope

- Terraform for declarative infrastructure
- Ansible for host and service configuration
- Kubernetes for workload orchestration
- Aptly, GitOps, Bazel, BuildBuddy, and Cloudflare R2 delivery-adjacent infrastructure
- Adjacent virtualization docs for VM-centric environments

## Choose the workflow this way

- Desired-state infra with plans/state -> `terraform.md`
- Idempotent host/service configuration -> `ansible.md`
- Cluster workload lifecycle and policy -> `kubernetes.md`
- Package publication and repository promotion -> `aptly.md`
- Bazel workspace and remote cache/execution policy -> `bazel.md` and `buildbuddy.md`
- Git-driven environment promotion -> `gitops.md`
- R2-backed artifact publication or readback -> `cloudflare-r2.md`
- VM orchestration or host virtualization -> `../virtualization/overview.md`

## Enforce these guardrails

- Plan before apply.
- Keep secrets and state inventories scoped and protected.
- Keep provider, module, toolchain, and remote-service versions pinned and reviewable.
