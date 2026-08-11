# Domain router
Purpose: choose one platform or tooling router for domain-specific work for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.
Use this router when the task is mainly tied to one platform, toolchain, or operating surface.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Choose one domain
<!-- BEGIN:contents -->
- `$CODEX_HOME/index/domains/desktop/overview.md` — Desktop (domain router, overview)
- `$CODEX_HOME/index/domains/infra/overview.md` — Infra (domain router, overview)
- `$CODEX_HOME/index/domains/lang/overview.md` — Lang (domain router, overview)
- `$CODEX_HOME/index/domains/observability/overview.md` — Observability (domain router, overview)
- `$CODEX_HOME/index/domains/system/overview.md` — System (domain router, overview)
- `$CODEX_HOME/index/domains/vscode/overview.md` — Vscode (domain router, overview)
- `$CODEX_HOME/index/domains/web/overview.md` — Web (domain router, overview)
<!-- END:contents -->

## Quick mapping
- Host services, filesystems, kernel, GRUB, sysctl, USBGuard -> system
- Containers, virtualization, Kubernetes, IaC -> infra
- Elasticsearch, log pipelines, auditd, AIDE, CrowdSec -> observability
- Browser stacks, Wayland, desktop entries -> desktop
- React, Next.js, HTMX, SvelteKit, Vue, Nuxt -> web
- Go, TypeScript, HTML, shell-adjacent language guidance -> lang
- VS Code profiles, settings, or extensions -> vscode

## You must stop when
- Pick one domain router and then one entrypoint from it.
- If the task is mainly about execution process rather than platform specifics, route back to `$CODEX_HOME/index/core/overview.md`.
