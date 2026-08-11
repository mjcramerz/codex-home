# TypeScript
Purpose: tell the Codex coding agent how to use `docs/lang/typescript.md` as a runtime-pack surface and when to stop browsing.
Guidance for TypeScript project defaults and build hygiene.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/lang/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- Enable `strict` mode; avoid `any`.
- You must use `tsconfig` references for larger repos.
- You must keep build outputs out of source directories.
- You must keep runtime boundaries explicit (Node-only vs browser-safe modules).
- Encode untrusted inputs as `unknown` and narrow with validators at boundaries.

## Testing
- You must run typecheck in CI.
- You must prefer `eslint` + `tsc --noEmit` for fast feedback.
- You must prefer deterministic package-manager flows (`pnpm install --frozen-lockfile`, pinned Node version).

## Codex source alignment
- Codex currently uses TypeScript in tooling packages (`shell-tool-mcp`, `sdk/typescript`, `codex-cli`) with shared pnpm workspace conventions.
- You must keep pack guidance aligned with workspace scripts and lockfile-driven installs when updating TypeScript workflows.

See also:
- `overview.md`
- `../style/typescript.md`
- `$CODEX_HOME/templates/typescript/ts-lib/`
- `$CODEX_HOME/snippets/typescript/tsconfig.json`
- You must use skill lang-typescript.
- `$CODEX_HOME/index/domains/lang/languages.md`
- `$CODEX_HOME/index/domains/lang/typescript.md`
