#!/usr/bin/env python3
"""Check the installed custom runtime without launching a model turn or MCP tool.

Run after installation as the desktop account. No secrets or full config values
are printed. Resource paths are checked on the host; the preseed wrapper's
mount/network namespace still needs its own live acceptance tests.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tomllib


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path('/data/codex/usr/home/config.toml'))
    parser.add_argument('--binary', type=Path, default=Path('/data/codex/share/bin/codex'))
    args = parser.parse_args()
    checks = []
    def record(name, okay, detail):
        checks.append({'check': name, 'ok': bool(okay), 'detail': detail})
    try:
        data = tomllib.loads(args.config.read_text())
        record('installed configuration', True, str(args.config))
    except (OSError, ValueError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, indent=2)); return 1
    def visit(obj, key=''):
        if isinstance(obj, dict):
            for k, value in obj.items():
                if isinstance(value, str) and (k.endswith('_file') or k == 'model_catalog_json'):
                    record('configured file '+k, Path(value).is_file(), value)
                visit(value, k)
        elif isinstance(obj, list):
            for value in obj:visit(value, key)
    visit(data)
    for name, server in data.get('mcp_servers', {}).items():
        if server.get('enabled', True) and 'command' in server:
            command = server['command']
            record('MCP command '+name, os.access(command, os.X_OK) if '/' in command else shutil.which(command), command)
    node = data.get('mcp_servers', {}).get('node_repl', {}).get('env', {})
    for k in ('NODE_REPL_LAUNCHER', 'NODE_REPL_NODE_PATH', 'CODEX_CLI_PATH'):
        if k in node:record(k, os.access(node[k], os.X_OK), node[k])
    if node.get('NODE_REPL_TRUSTED_CODE_PATHS'):
        for path in node['NODE_REPL_TRUSTED_CODE_PATHS'].split(':'):
            record('trusted desktop resource', Path(path).exists(), path)
    if node.get('NODE_REPL_TRUSTED_SERVICES'):
        services = json.loads(node['NODE_REPL_TRUSTED_SERVICES'])
        if not isinstance(services, dict) or not all(isinstance(v, str) for v in services.values()):
            raise ValueError('NODE_REPL_TRUSTED_SERVICES is not a string map')
        for name, path in services.items():
            record('trusted desktop service '+name, Path(path).is_file(), path)
    for name, settings in data.get('marketplaces', {}).items():
        if settings.get('source_type') == 'local':
            record('local marketplace '+name, Path(settings['source']).is_dir(), settings['source'])
    host_node = data.get('shell_environment_policy', {}).get('set', {}).get('NODE')
    if host_node:record('host Node', os.access(host_node, os.X_OK), host_node)
    modules = ['Moo', 'MooX::HandlesVia', 'MooX::StrictConstructor', 'Types::Standard']
    if shutil.which('perl'):
        result = subprocess.run(['perl', *['-M'+m for m in modules], '-e', 'exit 0'], capture_output=True, timeout=20, check=False)
        record('Perl hook dependencies', result.returncode == 0, ', '.join(modules))
    else:record('Perl hook dependencies', False, 'perl not installed')
    if args.binary.is_file() and os.access(args.binary, os.X_OK):
        result = subprocess.run([str(args.binary), '--version'], capture_output=True, text=True, timeout=20, check=False)
        record('custom engine version command', result.returncode == 0, result.stdout.strip()[:240])
    else:record('custom engine', False, str(args.binary))
    result = {'ok': all(x['ok'] for x in checks), 'checks': checks,
              'not_tested': ['model entitlement', 'effective app-server config', 'MCP initialization', 'wrapper namespace access']}
    print(json.dumps(result, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    try:raise SystemExit(main())
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        print('runtime check failed: '+str(exc), file=sys.stderr); raise SystemExit(1)
