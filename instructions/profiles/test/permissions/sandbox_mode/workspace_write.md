# Sandbox behavior

Write only within the effective workspace roots and other explicitly granted paths. Check protected paths and the current policy rather than assuming every file below the repository is writable. Request additional permissions only through the supported flow.

Use the effective network setting reported by the client: {{network_access}}.
Do not infer network reachability or authorization from the sandbox label alone.
