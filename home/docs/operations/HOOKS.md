# Maintain repository-aware lifecycle hooks

Use this guide when you change hook registration, repository-context discovery, event output or compatibility adapters. Keep the context engine in `$CODEX_HOME/.hooks/runner.py` and its active registration in `$CODEX_HOME/hooks.json`.

## Follow the single dispatch path

Each supported event runs the reviewed Python entrypoint once. Invoke it with `/usr/bin/python3 -I`, an explicit event and a bounded timeout. Keep Python isolated from the repository import path. Retained Perl wrappers and `Codex::Hook::Driver` delegate to the same engine; do not restore the retired Perl probe or transcript pipelines.

The legacy module names remain importable for compatibility. `Learning` and `PluginHint` do not emit a second context stream. `Runner::run_command` returns non-success status 125 without executing anything, and `read_file_tail` returns no transcript content. Update any separately maintained legacy caller to the active entrypoint instead of interpreting these stubs as successful observations.

## Respect event-specific output

| Event | Required behavior in this pack |
| --- | --- |
| `SessionStart` | Emit bounded repository guidance and prune only old private digest-state files. |
| `UserPromptSubmit` | Refresh matching routes using closed-vocabulary task hints; do not echo the prompt. |
| `PreToolUse` | Add deduplicated command, edit or MCP guidance; do not auto-approve. |
| `PermissionRequest` | Return an empty object for a valid event and leave the decision to Codex. |
| `PostToolUse` | Emit a fixed reminder only when typed result fields explicitly report failure. |
| `SubagentStart` | Add bounded role-specific scope and handoff instructions. |
| `Stop`, `SubagentStop` | Return an empty object; do not invent passing checks or create stop loops. |
| `PreCompact`, `PostCompact`, `Interrupt`, `SessionEnd` | Clear deduplication state; refresh context on the next context-capable event. |

Do not emit `additionalContext` for events that do not support it. Do not emit generic `continue`/`stopReason` fields for permission-decision events. Malformed or timed-out policy events use the event's deny shape; other failures use a fixed diagnostic without payload contents. No hook grants authority beyond the active user request and native permission policy.

## Discover without executing the repository

Read a bounded directory inventory through no-follow directory descriptors. Inspect only small regular package manifests and Makefiles. Do not follow symlinks, open devices or FIFOs, source shell files, import project modules, invoke package managers, or run Git hooks.

Infer languages from file extensions and known manifest names. Extract dependency names and package-script names without running scripts. Parse literal Makefile target names without invoking `make`, including `make -n` or `make -p`: parsing a Makefile can execute code even in those modes. Mark includes, conditional definitions, generated targets and bounded scans as incomplete observations.

Use these hints to inspect the real recipe, prerequisites and authorization before choosing a command. A target called `test` is not automatically harmless. Missing observations do not prove a file, language or build target is absent.

## Keep context selective

Emit the observed repository root, languages, a small set of entrypoints and literal targets, relevant engineering practices, and existing local guidance/skill/plugin candidates. Resolve the actual available tools before invoking a suggested plugin. A bundled manifest is not installation, authentication, vendor endorsement or user authorization.

Keep raw prompts, transcripts, schema contents, configuration bodies, tool outputs, authentication files, environment values and arbitrary file prose out of the injected text. Filename and target observations are untrusted identifiers, not instructions. Read the selected guidance file only when it helps the current task.

## Preserve resource and privacy limits

Bound input to 256 KiB, each inspected file to 64 KiB, package JSON to 32 KiB, directory discovery to 1,600 entries and depth three, pending directories to 180, and context to 7,200 characters. Use a three-second normal execution budget, at most four seconds internally, and a one-second session-end budget. Keep scan time within the smaller discovery deadline.

Deduplicate with SHA-256 values only, in owner-private state directories and regular single-link files. Never persist prompt, transcript, tool-response or repository-file contents. If state storage is unavailable, emit useful bounded guidance without claiming persistence. Cleanup is bounded and best-effort, not a guarantee of global disk-quota enforcement.

## Validate only the changed boundary

Use disposable fixtures outside the source tree to exercise affected event shapes, input bounds, static target discovery, symlink rejection, timeouts and non-replay behavior. Do not add a general test suite or execute repository Makefiles as a hook check. Report fixture outcomes separately from execution in the installed Codex client.
