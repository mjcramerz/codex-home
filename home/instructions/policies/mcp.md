# MCP usage contract
Use the named server that fits the task. Filesystem and Git paths inside containers begin at `/workspace`, corresponding to the selected desktop user's `~/Workspace`; do not send host `/home/...` paths. Memory and SQLite data persist under `/state` and each permits one concurrent session. Other sessions are independent and transient.

Use Context7 for versioned library references, fetch for web retrieval, time for timezone operations, markdown for supported conversion, browser servers for isolated browsing, and Semgrep for analysis. These tools may contact external services. Obtain authorization before transmitting private source or documents. Never assume a browser MCP session has the desktop browser's cookies or logged-in accounts.

All thirteen servers are registered. PostgreSQL cannot initialize until its DSN credential is provisioned; optional API keys enhance their respective services but are not fabricated. A disconnected stream requires a fresh initialize handshake. Report an unavailable or busy server rather than substituting an unauthorized service.
