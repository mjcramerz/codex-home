# Templates overview

Use this template when you need templates overview in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Apply the following practices to choosing and applying templates in this pack.

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

- A selected template path from `/data/codex/usr/examples/templates/`.
- A deterministic apply checklist from `using-templates.md`.
- Template-specific Inputs/Outputs/Next steps from the chosen `overview.md`.

## Quick map

- Template catalog: `/data/codex/usr/examples/templates/OVERVIEW.md`
- Usage guide: `using-templates.md`
- Build workflow: `../workflows/build-an-app.md`
- Cloudflare R2 workflow: `../workflows/cloudflare-r2.md`
- Template plan: `$CODEX_HOME/plans/templates-library.md`

## Categories

- Common repo hygiene: `/data/codex/usr/examples/templates/common/`
- CI: `/data/codex/usr/examples/templates/ci/`
- Infrastructure: `/data/codex/usr/examples/templates/infra/`
- Observability: `/data/codex/usr/examples/templates/observability/`
- Prompts: `/data/codex/usr/examples/templates/prompts/`
- Containers: `/data/codex/usr/examples/templates/containers/`
- systemd: `/data/codex/usr/examples/templates/systemd/`
- Filesystems: `/data/codex/usr/examples/templates/filesystems/`
- System hardening: `/data/codex/usr/examples/templates/system/`
- Virtualization: `/data/codex/usr/examples/templates/virtualization/`
- Languages: `/data/codex/usr/examples/templates/python/`, `/data/codex/usr/examples/templates/rust/`, `/data/codex/usr/examples/templates/go/`, `/data/codex/usr/examples/templates/typescript/`, `/data/codex/usr/examples/templates/perl/`
- Desktop: `/data/codex/usr/examples/templates/desktop/`

## Next steps

1. Choose a template path from `/data/codex/usr/examples/templates/OVERVIEW.md`.
2. Apply it with the deterministic flow in `using-templates.md`.
3. Run the template's local verification commands before commit.
