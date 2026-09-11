# Python

Use this guide when you implement or review Python modules, CLIs, packaging or automation. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Read pyproject.toml, interpreter constraints, lockfiles and the affected callers. Reuse the project's environment and package manager; do not upgrade the system interpreter or globally install dependencies for a local code change.

**2.** Define types at public boundaries and validate external data before constructing domain objects. Separate parsing, pure transformations and side effects; use explicit exceptions rather than blanket catch-and-continue.

**3.** Use pathlib for paths, context managers for resources, subprocess argument lists with shell=False, explicit encodings, bounded reads and timeouts. Avoid eval, unsafe deserialization and module imports from untrusted working directories.

**4.** Use module loggers and structured context. Redact tokens and payloads, preserve exception causes, and avoid logging the same failure at every layer.

**5.** Check the narrow changed contract using existing lint, type and test commands. Compiling source proves syntax only; it does not validate imports, optional dependencies, live services or runtime behavior.

## Select related guidance

- `$CODEX_HOME/docs/style/overview.md`
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/index/OVERVIEW.md`
- `$CODEX_HOME/snippets/python/`
- `$CODEX_HOME/index/pack/style.md`
- `$CODEX_HOME/index/style/python.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
