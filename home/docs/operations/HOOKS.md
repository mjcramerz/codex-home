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
| `PostToolUse` | Record bounded edit/check/failure observations; emit a fixed reminder only when typed result fields explicitly report failure. |
| `SubagentStart` | Add bounded role-specific scope and handoff instructions. |
| `Stop`, `SubagentStop` | Emit deduplicated factual check/failure or handoff reminders; return empty during an active stop hook and never block completion. |
| `PreCompact` | Remind the model to preserve scope, decisions, changed paths and observed checks; refresh context digests while retaining observation flags. |
| `PostCompact`, `Interrupt` | Refresh context digests, retaining observations; return an empty object. |
| `SessionEnd` | Remove private session state and return empty, including when its working directory was removed. |

Validate input and output against the supplied event schemas, including `Interrupt`. `permission_mode` contains hook protocol values such as `default` and `acceptEdits`, not permission-profile names. Reject duplicate JSON keys, non-finite numbers and mismatched event names. Do not emit `additionalContext` for events that do not support it or generic `continue`/`stopReason` fields for permission events. Malformed or timed-out policy events use the event's deny shape; other failures use a fixed diagnostic without payload contents. Session-end failure remains empty because that event has no output schema. No hook grants authority beyond the current task and native policy.

`PreToolUse` emits a short reminder for each tool class; it does not rescan the repository on every call. Completion observations use explicit `isError` or integer exit-status fields, never guessed status from result text. Simple validation command recognition does not execute commands or claim success. Preserve earlier failed-check observations until session end and report whether they were resolved.

## Discover without executing the repository

Read a bounded directory inventory through no-follow directory descriptors. Inspect only small regular package manifests and Makefiles. Do not follow symlinks, open devices or FIFOs, source shell files, import project modules, invoke package managers, or run Git hooks.

Infer languages from file extensions and known manifest names. Extract dependency names and package-script names without running scripts. Parse literal Makefile target names without invoking `make`, including `make -n` or `make -p`: parsing a Makefile can execute code even in those modes. Mark includes, conditional definitions, generated targets and bounded scans as incomplete observations.

Use these hints to inspect the real recipe, prerequisites and authorization before choosing a command. A target called `test` is not automatically harmless. Missing observations do not prove a file, language or build target is absent.

## Keep context selective

Emit the observed repository root, languages, a small set of entrypoints and literal targets, relevant engineering practices, and existing local guidance/skill/plugin candidates. Resolve the actual available tools before invoking a suggested plugin. A bundled manifest is not installation, authentication, vendor endorsement or user authorization.

Keep raw prompts, transcripts, schema contents, configuration bodies, tool outputs, authentication files, environment values and arbitrary file prose out of the injected text. Filename and target observations are untrusted identifiers, not instructions. Read the selected guidance file only when it helps the current task.

## Preserve resource and privacy limits

Bound input to 256 KiB, each inspected file to 64 KiB, package JSON to 32 KiB, directory discovery to 1,600 entries and depth three, pending directories to 180, and context to 7,200 characters. Registration adds 2,000-token context limits at session/prompt/subagent boundaries and 600-token limits for tool events. Use a three-second normal budget, at most four seconds internally, and a one-second interrupt/session-end budget. Keep discovery within its smaller deadline.

Store only the latest SHA-256 digest per fixed context channel and fixed boolean observation flags, in private mode-0700 directories and mode-0600 single-link regular files. Use bounded reads and nonblocking locks; reject symlinks, special files and unsafe ownership or permissions. A context change followed by a return to earlier context emits again. Compaction/interruption clears digests while preserving observations. Never persist prompt, transcript, tool-response or repository-file contents. If storage is unavailable, emit bounded guidance without claiming persistence. Cleanup is bounded and best-effort, not global disk-quota enforcement.

## Validate only the changed boundary

Run `python3 -m unittest discover -s tests` and `prove home/.hooks/t` from the source checkout. Disposable fixtures exercise all twelve event contracts, malformed input, deadlines, static discovery, non-replay, compaction/interruption, completion reminders, private state, unsafe filesystem objects and retained Perl dispatch. Never execute a repository Makefile as a hook discovery check. Report fixtures separately from execution in the installed Codex client.
