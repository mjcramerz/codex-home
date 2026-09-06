# Verification contract
Run focused tests for the changed behavior and relevant broader checks. Test malformed input, permission failures, unavailable dependencies, timeouts, cancellation, concurrent access and cleanup where they matter. For packaging, inspect the actual archive and verify executable modes, expected files and checksums.

Record commands, exit status and results. State which checks used mocks, which ran against real services, and which were not run. For deployment work, validate rendered systemd units and client configuration before activation, then perform live initialize/tools-list and functional probes. A failed check remains a failure until fixed or explicitly documented; never silently skip a required server or credential.
