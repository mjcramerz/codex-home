# Apply a focused patch

Use the advertised patch tool to edit text files. Read the target and surrounding
code first, preserve unrelated changes, and verify the resulting diff. Do not
assume a shell executable named `apply_patch` exists when the client exposes a
native tool instead.

Use the patch format accepted by the active tool. For the standard Codex format,
wrap operations in `*** Begin Patch` and `*** End Patch`. Use `*** Add File: path`,
`*** Update File: path`, or `*** Delete File: path` as appropriate. Prefix added
lines with `+`, removed lines with `-`, and unchanged context with a space. For an
update, supply enough exact context to identify the intended hunk unambiguously.

For example, adapt this format to an authorized existing file:

```text
*** Begin Patch
*** Update File: src/example.py
@@
-old_value = 1
+old_value = 2
*** End Patch
```

Do not paste patch payloads into an interpolated shell command. Validate paths,
keep edits inside the authorized scope, and preserve encoding and file modes.
Re-read changed sections and run the permitted check for the changed contract.
