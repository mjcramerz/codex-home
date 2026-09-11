# Go

Use this guide when you change Go packages, modules, CLIs or services. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Read go.mod, go.sum and workspace settings, then trace the affected API and callers. Keep module paths, public interfaces and supported Go versions stable unless the task changes them.

**2.** Propagate context for cancellation and deadlines. Close response bodies and files, stop tickers, and ensure every goroutine has a termination path.

**3.** Return wrapped errors with useful context; distinguish cancellation, not-found and invalid input. Avoid panic for expected external failures.

**4.** Use structured logging without credentials, bound network and parser inputs, and protect shared state with clear ownership or synchronization.

**5.** Use existing gofmt, go vet and focused go test commands; run the race detector when relevant and available. Report coverage limitations for external dependencies and unsupported platforms.

## Select related guidance

- `$CODEX_HOME/docs/lang/overview.md`
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/index/OVERVIEW.md`
- `$CODEX_HOME/templates/go/cli-app/`
- `$CODEX_HOME/snippets/go/main.go`
- `$CODEX_HOME/index/domains/lang/languages.md`
- `$CODEX_HOME/index/domains/lang/go.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
