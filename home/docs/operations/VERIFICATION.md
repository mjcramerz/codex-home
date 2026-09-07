# Evidence levels

`make verify` is offline validation: schema and semantic checks, reference integrity,
instruction mirrors, source syntax, unit regression tests, protocol relay tests,
MCP registration and systemd parser checks. It is not live deployment evidence.

`make test-hooks` executes actual Perl hooks when all Perl dependencies are present.
`make check-runtime` inspects installed binary/resource prerequisites without a model
turn. MCP `make smoke` initializes every local server, lists tools, exercises
filesystem writes in a disposable Workspace subdirectory and checks browser launch.
PostgreSQL requires a provisioned test account and reachable database. SSH smoke
must run from a native host session, not isolated Bubblewrap loopback.

Store target test logs privately. Never include credentials or private workspace
content in a bug report. Report skipped checks and exact reasons; do not replace a
failure with a passing static check or loosen confinement silently.
