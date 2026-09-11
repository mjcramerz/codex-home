# Next.js

Use this guide when the task concerns next.js. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to SSR/ISR React apps with Next.js.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Keep server/client boundaries explicit.
- Use route segments and layouts consistently.
- Avoid leaking secrets into client bundles.
- Keep side effects and data-fetching in server components where possible.
- Validate runtime config at startup and fail closed on missing secrets.

## Performance

- Prefer streaming and incremental rendering where supported.
- Keep API routes slim; move heavy work to workers.

## Validation checklist

- Run `pnpm lint`, `pnpm test`, and `pnpm build` with production env defaults.
- Verify route handlers enforce authz/input validation and bounded I/O.
- Check caching policy (`revalidate`, headers, ISR paths) for correctness and stale-data behavior.
- Confirm client bundles exclude server-only modules and secrets.

See also:
- `overview.md`
- `react.md`
- `$CODEX_HOME/templates/web/nextjs-app/`
- Read the `web-nextjs` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/nextjs.md`
