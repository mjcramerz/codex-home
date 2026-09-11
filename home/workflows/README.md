# Select an execution workflow

Use a workflow only when it matches the current task and its prerequisites are available. Read the relevant entrypoint, adapt its paths to the actual repository and preserve the user's allowed scope.

For MCP deployment, read [the deployment workflow](mcp-deployment.md) and distinguish configuration edits from installation, authentication and live tool execution. For domain workflows, use `$CODEX_HOME/docs/workflows/` through the central index.

Do not run commands solely because they appear in a workflow. Inspect their targets and side effects, use existing verification commands where relevant, and report skipped or blocked steps without inventing success.
