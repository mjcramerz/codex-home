# Shell runtime boundaries

Use this guide when you change POSIX shell, Bash or zsh scripts and repository automation. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Inspect the shebang and declared interpreter. Keep POSIX sh free of Bash or zsh extensions; select Bash explicitly when arrays or other Bash features are required.

**2.** Quote expansions, use -- before untrusted operands where supported, prefer argument arrays in Bash, and never use eval to dispatch user input. Avoid parsing ls or splitting filenames on whitespace.

**3.** Check failures explicitly around expected fallible operations. Do not assume set -e, pipelines or subshells give uniform error propagation across shells; isolate deliberate nonzero statuses.

**4.** Use private temporary directories and cleanup traps scoped to paths you created. Resolve and check destructive targets, reject empty paths, and preserve caller-owned files.

**5.** Keep stdout machine-readable when required, send redacted diagnostics to stderr and bound command duration. Run the matching interpreter's syntax check and existing ShellCheck/tests where available.

## Select related guidance

- `$CODEX_HOME/docs/style/bash.md`
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/index/style/overview.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
