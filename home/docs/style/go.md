# Go style guide
Purpose: tell the Codex coding agent how to use `docs/style/go.md` as a runtime-pack surface and when to stop browsing.
Canonical Go guidance for this pack. Follow repo-specific conventions first.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/style/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline
- You must use `gofmt` and `goimports` in CI.
- You must keep packages small and cohesive.
- You must prefer explicit errors over panic; wrap with context.

## Security
- You must validate inputs at boundaries; enforce size limits.
- Set timeouts on all network calls.

## Testing
- You must prefer table-driven tests.
- You must keep tests deterministic and fast.

## References
- `overview.md`
- Snippets: `$CODEX_HOME/snippets/go/`
- Template: `$CODEX_HOME/templates/go/cli-app/`
- `$CODEX_HOME/index/pack/style.md`
- `$CODEX_HOME/index/style/go.md`
