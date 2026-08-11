You must now assume the role of a senior software developer with decades of experience in working with Debian, Codex from OpenAI, Python, Perl, Shell scripting, Podman, and Model Context Protocol. This 
repo contains the code base for installing and managing Codex from OpenAI. The code base also deploy codex-mcp with mutltiple mcp tools! You have extensive knowledge in working with Codex from OpenAI, 
Podman and MCP tools. Your goal with this task is to complete all of the objectives outlined in numeric order below:
1. Your first objective must focus on resolving the occuring issues with codex-mcp and podman! You must make sure that everything are incorporated properly and correct!! The following errors must be resolved: 
[install] installing codex runtime wrapper
[install] installing managed secret helper
[install] installing codex login wrapper
[install] installing codex MCP token wrapper
[install] installing shell completion files
[install] installing schema helper wrappers
[ok] install complete
[make] install -> deploying the installed codex-mcp runtime
[ok] codex-mcp preflight passed
ERROR: pinned MCP image dispatcher verification failed: time="2026-07-31T22:15:21Z" level=warning msg="The cgroupv2 manager is set to systemd but there is no systemd user session available"
time="2026-07-31T22:15:21Z" level=warning msg="For using systemd, you may need to log in using a user session"
time="2026-07-31T22:15:21Z" level=warning msg="Alternatively, you can enable lingering with: `loginctl enable-linger 997` (possibly as root)"
time="2026-07-31T22:15:21Z" level=warning msg="Falling back to --cgroup-manager=cgroupfs"
Failed to re-execute libcrun via memory file descriptor
time="2026-07-31T22:15:21Z" level=error msg="Removing container 9d5e3310a6019b60a7a7990884c9ecc90e8aa97763150641981fc8d9d9518749 from runtime after creation failed"
Error: OCI runtime error: crun: Failed to re-execute libcrun via memory file descriptor
make: *** [Makefile:75: install] Error 1
2. Your second objective must focus on setting /data/codex to owner and group as 
the current user invoking 'make ...'. The change of permission on this folder must be done with sudo!

You must now start your task immediately and make sure everything are incorporated properly and correct!!
