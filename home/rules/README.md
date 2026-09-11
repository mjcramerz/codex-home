# Execution rules

Apply the following execution rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

No global allow-all rule is shipped. Repository-specific prefix rules should be narrow, reviewed and kept with the project. Codex approvals, managed requirements, MCP tool approvals and OS confinement are separate controls. A hook is not a security sandbox and must not be used as an authorization substitute.
