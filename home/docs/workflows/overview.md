# Workflow catalog
Purpose: map recurring task types to operational playbooks and help the agent choose one workflow before editing for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Workflow catalog
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/workflows/agent-orchestration.md` — Agent orchestration workflow
- `$CODEX_HOME/docs/workflows/planning.md` — Planning workflow
- `$CODEX_HOME/docs/workflows/memory-runtime.md` — Memory routing and retired-flow cleanup workflow
- `$CODEX_HOME/docs/workflows/cloudflare-r2.md` — Cloudflare R2 workflow
- `$CODEX_HOME/docs/workflows/debian-preseed.md` — Debian preseed workflow
- `$CODEX_HOME/docs/workflows/ci-cd.md` — CI/CD workflow
- `$CODEX_HOME/docs/workflows/gitlab-ci.md` — GitLab CI/CD workflow
- `$CODEX_HOME/docs/workflows/gitlab-runner.md` — GitLab Runner workflow
- `$CODEX_HOME/docs/workflows/aptly.md` — Aptly workflow
- `$CODEX_HOME/docs/workflows/bazel-buildbuddy.md` — Bazel and BuildBuddy workflow
- `$CODEX_HOME/docs/workflows/gitops.md` — GitOps workflow
- `$CODEX_HOME/docs/workflows/labwc.md` — Labwc workflow
- `$CODEX_HOME/docs/workflows/waybar.md` — Waybar workflow
- `$CODEX_HOME/docs/workflows/wofi.md` — Wofi workflow
- `$CODEX_HOME/docs/workflows/crystal-dock.md` — Crystal Dock workflow
- `$CODEX_HOME/docs/workflows/rust-toolchain.md` — Rust toolchain workflow
- `$CODEX_HOME/docs/workflows/testing.md` — Testing workflow
- `$CODEX_HOME/docs/workflows/repo-ops.md` — Repo operations workflow
<!-- END:contents -->

## You must choose the workflow this way
- Multi-agent routing and handoff design -> `agent-orchestration.md`
- Plan creation, validation ladders, and rollout shape -> `planning.md`
- Repo-aware memory routing or retired memory-flow cleanup -> `memory-runtime.md`
- Cloudflare R2-backed artifact publication or readback -> `cloudflare-r2.md`
- Debian installer trees and unattended install contracts -> `debian-preseed.md`
- GitLab runner host/service policy -> `gitlab-runner.md`
- Aptly publication and retention contracts -> `aptly.md`
- Bazel / BuildBuddy CI acceleration -> `bazel-buildbuddy.md`
- Git-driven promotion and reconciliation flows -> `gitops.md`
- Labwc compositor/session work -> `labwc.md`
- Waybar module or restart work -> `waybar.md`
- Wofi launcher or command-safety work -> `wofi.md`
- Crystal Dock start/restart behavior -> `crystal-dock.md`
- Cargo, rustc, and rustup policy -> `rust-toolchain.md`

## You must maintain this file by following these rules
- Every workflow added here should have a corresponding plan under
  `$CODEX_HOME/plans/workflows/` when the execution path is non-trivial.
- Keep workflow guidance platform- or domain-scoped and free of machine-local
  source-tree routes.
