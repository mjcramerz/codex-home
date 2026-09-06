# Engineering practice
Understand the existing interface and tests before changing behavior. Prefer the smallest coherent change that meets the request; preserve user edits and public contracts unless a migration is explicitly part of the task. Validate input types, sizes, ranges, paths, ownership and trust boundaries before mutation.

Use direct argument vectors rather than shell evaluation. Quote shell expansions, select the required shell explicitly, use Python standard-library facilities where sufficient, and avoid dependencies solely for trivial tasks. In Rust, make ownership and error propagation explicit; do not add unsafe code without a documented invariant and focused tests. In TOML, reject obsolete or unknown keys instead of assuming they are honored.

For daemons, specify startup and shutdown ordering, signal behavior, timeouts, resource budgets, lock ownership, atomic replacement, partial-failure cleanup and restart semantics. A stdio MCP stream is per connection: restarting a process cannot transparently resume a protocol session. Log bounded metadata, not credentials or arbitrary tool payloads.
