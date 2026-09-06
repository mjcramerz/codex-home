# Security and permission boundaries
Use the narrowest effective filesystem, network and credential access. Keep authentication in the client or designated secret store. Never print secrets, put them in command arguments, commit them, or copy a desktop home, SSH agent, session bus or container engine socket into an MCP container.

A writable filesystem MCP server is an external capability: Codex shell read-only settings alone do not make its tools read-only. Check tool approvals and server mounts. Full-access configuration is an explicit operator choice, not an instruction to approve every action. Do not disable AppArmor, browser sandboxing, SSH host-key checking, TLS verification or managed policy merely to make a test pass.

Treat the devops group as a trusted engine-administration group, not a tenant-isolation boundary. Members can control that account's rootless Podman engine. Containers run as named user devops and must never mount the engine socket. Use database permissions in addition to SQL read-only hints. Explain remaining risks and test limitations accurately.
