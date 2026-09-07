# Plugin and hook lifecycle

Keep plugin manifests and local marketplace entries consistent with their source
files. `make verify` checks catalog coverage; it does not certify every external
plugin or remote service as safe or reachable. Review origin, requested tools,
credential scope and execution permissions before enabling new code. Versioned
bundled browser assets must match the installed desktop app.

Do not modify product-managed caches during a running session. Asset installation
backs up overwritten files and preserves unrelated runtime data. Existing app
preferences are merged; secrets, auth databases and session history are not reset.

Lifecycle hooks execute trusted local code, not downloaded instructions. The bounded
hook runner enforces JSON framing, input/output caps, timeouts and process-group
cleanup. PreToolUse and PermissionRequest infrastructure failures fail closed;
non-policy notification failures emit a generic warning and no private payload.
Hook logs must not contain prompts, command arguments, tokens or raw tool output.
Install the documented Perl dependencies before enabling the real hooks.
