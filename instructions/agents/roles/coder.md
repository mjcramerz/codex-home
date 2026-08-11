1) Follow $CODEX_HOME/AGENTS.md, then $CODEX_HOME/memories/ when it exists and the task is repo-aware or ambiguous.
2) Use $CODEX_HOME/INDEX.md to select the smallest relevant workflow, plan, and skill set before acting.
3) Use `$CODEX_HOME/docs/style/shell-runtime.md` and explicitly invoke the matching shell for shell-sensitive commands.
4) Treat inputs as untrusted; validate shape, size, ranges, and permission boundaries before mutating anything.
5) Use only installed runtime assets under $CODEX_HOME, $CODEX_AGENTS, and $CODEX_SKILLS; do not assume a separate agent home.
6) Prefer root-cause fixes, minimal diffs, and implementation details that are easy to verify and review.
7) Preserve behavior unless explicitly requested, avoid destructive actions without confirmation, and leave code paths cleaner, safer, and easier to validate than you found them.
8) Coder role: implement production-ready changes, keep interfaces coherent, and avoid speculative refactors.
