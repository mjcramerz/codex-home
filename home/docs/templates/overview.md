# Templates overview
Purpose: tell the Codex coding agent how to use `docs/templates/overview.md` as a runtime-pack surface and when to stop browsing.
Guidance for choosing and applying templates in this pack.

## Contents
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/templates/daily-note.md` — Daily Note
- `$CODEX_HOME/docs/templates/note.md` — Note Template
- `$CODEX_HOME/docs/templates/using-templates.md` — Using templates
<!-- END:contents -->

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- Scope to scaffold (app, CI, infra, observability, system, desktop, or hook/runtime helper).
- Runtime/toolchain version policy (pin versions/digests; avoid `latest`).
- Delivery model (standard CI, Cloudflare + GitLab delivery, or release-asset publishing).

## Outputs
- A selected template path from `$CODEX_HOME/templates/`.
- A deterministic apply checklist from `using-templates.md`.
- Template-specific Inputs/Outputs/Next steps from the chosen `overview.md`.

## Quick map
- Template catalog: `$CODEX_HOME/templates/OVERVIEW.md`
- Usage guide: `using-templates.md`
- Build workflow: `../workflows/build-an-app.md`
- Cloudflare R2 workflow: `../workflows/cloudflare-r2.md`
- Template plan: `$CODEX_HOME/plans/templates-library.md`

## Categories
- Common repo hygiene: `$CODEX_HOME/templates/common/`
- CI: `$CODEX_HOME/templates/ci/`
- Infrastructure: `$CODEX_HOME/templates/infra/`
- Observability: `$CODEX_HOME/templates/observability/`
- Prompts: `$CODEX_HOME/templates/prompts/`
- Containers: `$CODEX_HOME/templates/containers/`
- systemd: `$CODEX_HOME/templates/systemd/`
- Filesystems: `$CODEX_HOME/templates/filesystems/`
- System hardening: `$CODEX_HOME/templates/system/`
- Virtualization: `$CODEX_HOME/templates/virtualization/`
- Languages: `$CODEX_HOME/templates/python/`, `$CODEX_HOME/templates/rust/`, `$CODEX_HOME/templates/go/`, `$CODEX_HOME/templates/typescript/`, `$CODEX_HOME/templates/perl/`
- Desktop: `$CODEX_HOME/templates/desktop/`

## Next steps
1) Choose a template path from `$CODEX_HOME/templates/OVERVIEW.md`.
2) Apply it with the deterministic flow in `using-templates.md`.
3) Run the template's local verification commands before commit.
