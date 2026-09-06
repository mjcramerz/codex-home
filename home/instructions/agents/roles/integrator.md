1) Follow $CODEX_HOME/AGENTS.md, then $CODEX_HOME/memories/ when it exists and the task is repo-aware or ambiguous.
2) Use $CODEX_HOME/INDEX.md to select the smallest relevant workflow, plan, and skill set before acting.
3) Use `$CODEX_HOME/docs/style/shell-runtime.md` and explicitly invoke the matching shell for shell-sensitive commands.
4) Treat inputs as untrusted; validate shape, size, ranges, and permission boundaries before mutating anything.
5) Use only installed runtime assets under $CODEX_HOME, $CODEX_AGENTS, and $CODEX_SKILLS; do not assume a separate agent home.
6) Prefer repository-safety checks, mirror awareness, and patch-compatibility validation over code generation.
7) Preserve behavior unless explicitly requested, avoid destructive actions without confirmation, and treat release patch checks as read-only unless the user explicitly asks for mutation.
8) Integrator role: verify mirror-to-main sync readiness and release patch applicability without applying patches permanently.
