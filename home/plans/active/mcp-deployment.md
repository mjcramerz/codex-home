# MCP deployment acceptance plan

Use this plan when you need to carry out mcp deployment acceptance work. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

1. Confirm the desktop account, devops socket, cgroup v2, immutable image reference,
   profile digest and Workspace ACL support with preflight.
2. Install protected code, generate/preserve SSH identity and host key, build the
   derived image, verify image ID and start the socket-activated target.
3. Provision only required credentials; initialize all 13 server modes. Verify
   read/write Workspace behavior and per-server credential/mount isolation.
4. Run browser launch, SSH, toolchain execution, concurrent-client and stop/restart
   tests. Verify no orphaned containers, leaked credential directories or port binds.
5. Back up state, test restore to empty state, and record live acceptance evidence.

An offline source review completes none of steps 1-5 on an actual target machine.
