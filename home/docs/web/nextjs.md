# Next.js
Purpose: tell the Codex coding agent how to use `docs/web/nextjs.md` as a runtime-pack surface and when to stop browsing.
Guidance for SSR/ISR React apps with Next.js.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must keep server/client boundaries explicit.
- You must use route segments and layouts consistently.
- Avoid leaking secrets into client bundles.
- You must keep side effects and data-fetching in server components where possible.
- You must validate runtime config at startup and fail closed on missing secrets.

## Performance
- You must prefer streaming and incremental rendering where supported.
- You must keep API routes slim; move heavy work to workers.

## Validation checklist
- You must run `pnpm lint`, `pnpm test`, and `pnpm build` with production env defaults.
- You must verify route handlers enforce authz/input validation and bounded I/O.
- You must check caching policy (`revalidate`, headers, ISR paths) for correctness and stale-data behavior.
- You must confirm client bundles exclude server-only modules and secrets.

See also:
- `overview.md`
- `react.md`
- `$CODEX_HOME/templates/web/nextjs-app/`
- You must use skill web-nextjs.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/nextjs.md`
