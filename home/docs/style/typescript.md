# Typescript

Use this guide when you change TypeScript or JavaScript applications, tooling or packages. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Inspect package.json, the single authoritative lockfile, tsconfig, runtime versions and actual script definitions. Use the existing package manager and avoid unrelated dependency refreshes.

**2.** Keep strict types at module boundaries; treat network, JSON and environment values as unknown until validated. Do not replace a type error with any or an unchecked assertion.

**3.** Handle rejected promises, cancellation and cleanup. Bound requests and retries, and avoid event-listener leaks or unbounded concurrency.

**4.** Keep server credentials out of client bundles and logs. Validate URLs and output contexts, and preserve CSP, authentication and authorization boundaries.

**5.** Use the existing typecheck, lint, unit and build scripts after reading their commands. A script name is only a candidate until its side effects and prerequisites are understood.

## Select related guidance

- `$CODEX_HOME/docs/style/overview.md`
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/index/OVERVIEW.md`
- `$CODEX_HOME/snippets/typescript/`
- `$CODEX_HOME/templates/typescript/ts-lib/`
- `$CODEX_HOME/index/pack/style.md`
- `$CODEX_HOME/index/style/typescript.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
