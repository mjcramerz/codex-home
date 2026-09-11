# Logging and error evidence

Use this guide when you add or modify logging, telemetry, audit events or error reporting.

## Implementation

Identify producers, consumers, field contracts, retention requirements and sensitive-data boundaries. Preserve compatibility for existing dashboards, alerts and downstream parsers.

Use structured events with stable names, severity and correlation identifiers. Redact at the source and ingestion boundary; never log credentials, complete environments or unrestricted request bodies.

Bound message size, cardinality, buffering and retries. Define behavior for disk exhaustion or an unavailable collector without silently losing critical failures.

Use rotation and retention appropriate to the platform; verify ownership, reopen behavior and archival access. Avoid exposing unauthenticated log or metrics endpoints.

Validate representative success, error and redaction paths with existing fixtures. Distinguish configuration validity from actual delivery, searchability and alert behavior.

## Routing

Read `$CODEX_HOME/docs/observability/overview.md` for the specific collector or storage system. Read `$CODEX_HOME/docs/security/overview.md` when the change crosses a sensitive-data boundary.
