# TypeScript style guide
Purpose: tell the Codex coding agent how to use `docs/style/typescript.md` as a runtime-pack surface and when to stop browsing.
Canonical TypeScript guidance for this pack. Follow repo-specific conventions first.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/style/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline
- Enable `strict` mode and avoid `any`.
- You must prefer `unknown` over `any` for untrusted data.
- You must keep `tsconfig.json` explicit and minimal.
- Enable `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` when feasible.

## Structure
- Separate runtime code from type-only modules.
- You must prefer composable utilities over large helpers.
- You must keep ESM/CJS boundaries explicit and avoid ambiguous package exports.

## Web-stack notes
- React/Next.js/HTMX projects should share strict TypeScript defaults and CI typechecks.
- Enforce stable frontend build commands (`lint`, `typecheck`, `test`, `build`) in one documented path per project.

## References
- `overview.md`
- Snippets: `$CODEX_HOME/snippets/typescript/`
- Template: `$CODEX_HOME/templates/typescript/ts-lib/`
- `$CODEX_HOME/index/pack/style.md`
- `$CODEX_HOME/index/style/typescript.md`
