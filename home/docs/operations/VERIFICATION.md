# Verify only the contract you changed

Use this guide when a task requires evidence that an edit works. Honor explicit limits on tests, new files, network calls and live environments; this guide does not authorize a general validation campaign.

## Choose a relevant check

Trace the changed input, behavior and output to an existing command or a small disposable fixture. Read the command, its prerequisites and its side effects first. Discover literal Makefile targets without running Make merely for discovery. Do not assume `make check`, `make verify`, `make generate` or any test directory exists.

Use the declared toolchain. Parse TOML/JSON/YAML with the intended parser, compile Python without importing project modules, and choose the shell named by the shebang. Inspect Perl compile-time blocks before `perl -c`; a syntax command can execute initialization code.

For hooks, exercise the affected event and bounded malformed-input cases outside the repository. For instructions, preserve template placeholders and output contracts, resolve local references, and check that mirror copies do not contradict their source. Keep schemas out of normal assistant context.

## Interpret the result accurately

A parse proves syntax, not supported keys. A schema match does not prove client acceptance or credential availability. A fixture does not prove a live service. A passing unit test does not establish deployment health or all-platform compatibility.

Report the exact command, result and relevant limitation. Distinguish passed, failed and not run. Do not fill a report with invented logs, assumed Makefile targets or promises to finish after the turn.

## Keep the tree clean

Do not add root-level reports, general test suites or verification files without authorization. Place disposable fixtures and parser caches outside the source tree, and package only the intended repository files. Preserve out-of-scope files and existing user work.
