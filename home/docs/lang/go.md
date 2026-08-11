# Go
Purpose: tell the Codex coding agent how to use `docs/lang/go.md` as a runtime-pack surface and when to stop browsing.
Guidance for Go module structure and operational defaults.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/lang/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must use modules (`go.mod`) and keep dependencies minimal.
- You must prefer `cmd/<app>` for binaries and `internal/` for private packages.
- You must add context/timeouts to network calls.

## Testing
- You must keep unit tests fast and deterministic.
- You must use `go test ./...` in CI with `-race` where feasible.

See also:
- `overview.md`
- `../style/go.md`
- `$CODEX_HOME/templates/go/cli-app/`
- `$CODEX_HOME/snippets/go/main.go`
- You must use skill lang-go.
- `$CODEX_HOME/index/domains/lang/languages.md`
- `$CODEX_HOME/index/domains/lang/go.md`
