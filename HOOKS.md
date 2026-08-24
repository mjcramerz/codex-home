# Codex Hook Runtime on Debian

This repository ships the hook registry and Perl runtime that are installed
under `$CODEX_HOME`. The implementation is repository-relative and does not
depend on one fixed value for `$CODEX_HOME`.

## Runtime layout

- `home/hooks.json` is the installed hook registry. It registers all current
  lifecycle events represented by the checked-in input schemas:
  `SessionStart`, `SessionEnd`, `UserPromptSubmit`, `PreCompact`,
  `PostCompact`, `Stop`, `PreToolUse`, `PermissionRequest`, `PostToolUse`,
  `SubagentStart`, and `SubagentStop`.
- `home/.hooks/scripts/*.pl` contains thin event and profile wrappers. Registry
  commands invoke these wrappers as:

  ```text
  perl "$CODEX_HOME/.hooks/scripts/<wrapper>.pl"
  ```

  Quoting `$CODEX_HOME` keeps paths with spaces safe and avoids hard-coding a
  deployment location.
- `home/.hooks/scripts/hook_driver.pl` is the shared command boundary. It reads
  one JSON object from standard input, dispatches the selected lifecycle event,
  and converts runtime failures into bounded advisory hook output.
- `home/.hooks/modules/Codex/Hook/*.pm` contains validation, policy, context,
  repository, plugin, and output logic. Side effects remain in the wrappers and
  driver; reusable parsing and rendering logic stays in modules.
- `generate/schemas/*.command.input.schema.json` is the repository schema source for
  hook input. `home/.hooks/schema/generated/*.command.input.schema.json` is the
  installed runtime mirror and must remain byte-identical to the root schema
  set.
- `home/.hooks/modules/Codex/Hook/HookManifest.toml` records singleton events,
  tool profiles, wrapper names, matchers, status messages, and timeouts for
  audit and generation checks.

## Typed Moo boundary

`home/.hooks/modules/Codex/Hook/Event.pm` wraps every normalized lifecycle
payload before event-specific logic runs:

- `Moo` provides the immutable constructor and accessors.
- `MooX::StrictConstructor` rejects unknown constructor keys instead of
  silently accepting misspelled attributes.
- `Types::Standard` constrains `event_arg` to `Str` and `payload` to `HashRef`.
- `MooX::HandlesVia` delegates only the required hash operations through the
  documented `handles_via => 'Hash'` attribute option.
- Construction eagerly resolves the canonical event name, so unsupported
  lifecycle event names fail at the object boundary.

Hook JSON is untrusted input. The driver normalizes it, constructs the typed
event object, and validates the normalized payload against the matching JSON
Schema before producing context or policy output.

## `SessionEnd`

`SessionEnd` is registered with matcher `^other$` and a three-second timeout.
It always runs synchronously. A valid payload is schema-validated and produces
no standard output or standard error, so normal Codex shutdown is not polluted
with unnecessary context. Invalid input is converted by the shared driver into
one bounded advisory JSON response instead of terminating Codex.

## Debian Perl packages

Install the runtime and the modules used directly by the hook object boundary:

```bash
sudo apt-get update
sudo apt-get install --no-install-recommends \
  perl \
  libmoo-perl \
  libmoox-handlesvia-perl \
  libmoox-strictconstructor-perl \
  libtype-tiny-perl
```

`libtype-tiny-perl` provides `Types::Standard`. These are Debian package names;
the repository does not inspect or depend on whichever modules happen to be
installed on the machine used to prepare this source tree.

## Validation

Run these checks from the repository root after installing the packages above.

### Parse the registry and manifest

```bash
python3 -m json.tool home/hooks.json >/dev/null
python3 - <<'PY'
from pathlib import Path
import tomllib

with Path("home/.hooks/modules/Codex/Hook/HookManifest.toml").open("rb") as handle:
    tomllib.load(handle)
PY
```

### Verify the runtime schema mirror

```bash
python3 - <<'PY'
from pathlib import Path

source = Path("schemas")
mirror = Path("home/.hooks/schema/generated")
pattern = "*.command.input.schema.json"
source_files = {path.name: path for path in source.glob(pattern)}
mirror_files = {path.name: path for path in mirror.glob(pattern)}

assert source_files.keys() == mirror_files.keys()
for name, source_path in source_files.items():
    assert source_path.read_bytes() == mirror_files[name].read_bytes(), name
PY
```

### Compile and test the Perl runtime

```bash
perl -Ihome/.hooks/modules -c home/.hooks/modules/Codex/Hook/Event.pm
perl -Ihome/.hooks/modules -c home/.hooks/modules/Codex/Hook/Driver.pm
prove -Ihome/.hooks/modules -v home/.hooks/t/event.t

while IFS= read -r -d '' file; do
  perl -Ihome/.hooks/modules -c "$file"
done < <(
  find home/.hooks -type f \( -name '*.pm' -o -name '*.pl' \) -print0
)
```

### Verify silent `SessionEnd`

```bash
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

printf '%s\n' \
  '{"cwd":".","hook_event_name":"SessionEnd","reason":"other","session_id":"validation","transcript_path":null}' \
  | CODEX_HOME="$PWD/home" perl home/.hooks/scripts/session_end.pl \
      >"$tmpdir/stdout" 2>"$tmpdir/stderr"

test ! -s "$tmpdir/stdout"
test ! -s "$tmpdir/stderr"
```
