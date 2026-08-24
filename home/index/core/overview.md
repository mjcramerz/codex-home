# Core router
Purpose: choose one workflow-level entrypoint for cross-cutting or ambiguous work for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.
Use this router for workflow-level work that is not primarily domain specific.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Route here when
- you need planning, testing, security, CI/CD, repo operations, performance, or supply-chain guidance
- the task spans multiple domains and needs one coordinating workflow
- the task is ambiguous and you need a safe execution frame before editing

## Choose one entrypoint
<!-- BEGIN:contents -->
- `$CODEX_HOME/index/core/agent-orchestration.md` — Agent orchestration workflow (entrypoint)
- `$CODEX_HOME/index/core/ci-cd.md` — CI/CD workflow (entrypoint)
- `$CODEX_HOME/index/core/execpolicy.md` — Execpolicy workflow (entrypoint)
- `$CODEX_HOME/index/core/perf.md` — Performance playbook (entrypoint)
- `$CODEX_HOME/index/core/plan.md` — Planning workflow (entrypoint)
- `$CODEX_HOME/index/core/repo-ops.md` — Repo operations workflow (entrypoint)
- `$CODEX_HOME/index/core/review-hardening.md` — Review hardening checklist (entrypoint)
- `$CODEX_HOME/index/core/security.md` — Security overview (entrypoint)
- `$CODEX_HOME/index/core/supply-chain.md` — Supply-chain controls (entrypoint)
- `$CODEX_HOME/index/core/testing.md` — Testing workflow (entrypoint)
<!-- END:contents -->

## Do not route here when
- the work is clearly about one platform or tool family -> use `$CODEX_HOME/index/domains/overview.md`
- the work is about maintaining the runtime pack itself -> use `$CODEX_HOME/index/pack/overview.md`
- the work is only about language or shell conventions -> use `$CODEX_HOME/index/style/overview.md`
