# Python CLI Template (overview)
Purpose: tell the Codex coding agent how to use `templates/python/cli-app/overview.md` as a runtime-pack surface and when to stop browsing.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
pytest -q
python -m cli_app --help
python -m cli_app --version
pip install -e .
cli-app --help
```

## Logging
- `--log-format json` for structured logs (stderr)
- `-v` / `-vv` to increase verbosity
- `LOG_LEVEL` and `LOG_FORMAT` env vars override defaults

## Notes
- You must keep dependencies minimal and pinned.
- You must use `APP_` env prefix if you add settings.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs
- Files copied from this template directory.
- `.gitignore`
- `cli_app/`
- `pyproject.toml`
- `requirements-dev.txt`
- `tests/`

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, you must check related files
- Docs: `$CODEX_HOME/docs/style/python.md`
- Snippets: `$CODEX_HOME/snippets/python/`
