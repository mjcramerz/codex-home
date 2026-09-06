#!/usr/bin/python3
"""Git reads an opt-in token from the per-server credential mount."""
import sys
from pathlib import Path
prompt=sys.argv[1].lower() if len(sys.argv)==2 else ''
if 'username' in prompt:print('x-access-token')
elif 'password' in prompt:print(Path('/run/mcp-credentials/github-token').read_text().strip())
else:raise SystemExit(1)
