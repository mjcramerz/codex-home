# Execpolicy rules catalog
Purpose: explain how runtime execpolicy rules are organized, when to edit them, and what validation they require.

## Navigation
<!-- BEGIN:nav -->
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when
- you are changing command-allow or command-deny policy
- you need to understand which rules file owns a class of commands
- you are reviewing whether rule ordering or match coverage is still correct

## Design intent
- Keep routine engineering automation available without constant prompts.
- Keep explicit hard-deny coverage for destructive, privilege-escalating, or outage-causing commands.
- Keep rule ordering deterministic so policy decisions are reviewable.

## Rule evaluation
- The strictest matching decision wins.
- Broad allow rules belong in lower-numbered files.
- Hard-deny rules belong in `90-forbidden.rules`.
- When adding a new command family, place the allow rule in the closest domain file and add a deny rule when destructive variants are obvious.

## Rule files
- `$CODEX_HOME/rules/00-core.rules` — baseline shell and inspection tooling
- `$CODEX_HOME/rules/10-vcs.rules` — git and version-control operations
- `$CODEX_HOME/rules/12-scripting.rules` — language runtimes and script execution
- `$CODEX_HOME/rules/20-network.rules` — network, cloud, and remote-access tooling
- `$CODEX_HOME/rules/25-packages.rules` — package managers and toolchain installers
- `$CODEX_HOME/rules/30-system.rules` — filesystem, service, and host operations
- `$CODEX_HOME/rules/35-crypto.rules` — keys, certificates, and signing tools
- `$CODEX_HOME/rules/40-infra.rules` — containers, orchestration, and infra tooling
- `$CODEX_HOME/rules/90-forbidden.rules` — explicit hard-deny rules

## Rule schema
Rules use `prefix_rule(...)` with explicit `pattern`, `decision`, `match`, and optional `not_match` examples.

```toml
prefix_rule(
  pattern = ["git", "status"],
  decision = "allow",
  match = [
    ["git", "status", "--porcelain=v1"],
  ],
  not_match = [
    ["git", "status", "--ignored"],
  ],
)
```

## Editing checklist
- Keep command coverage broad enough for routine maintenance.
- Add explicit denies for risky subcommands and destructive forms.
- Include `match` / `not_match` examples so intent is self-tested.
- Re-run targeted validation plus the smallest syntax and contract checks for the touched rules surface after edits.

## Related
- `$CODEX_HOME/index/pack/rules.md`
- `$CODEX_HOME/docs/workflows/execpolicy.md`
