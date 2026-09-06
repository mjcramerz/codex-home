#!/usr/bin/env python3
"""Utility helper for the quality-code-review skill.

This script keeps workflow discovery deterministic and validates baseline skill wiring.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

import yaml

SKILL_NAME = 'quality-code-review'
SKILL_CATEGORY = 'AUDIT'
SKILL_DESCRIPTION = 'High-rigor code review skill: intent alignment, correctness, security, performance, and reproducibility checks with actionable output.'
LAST_REFRESH_UTC = '2026-02-11'
REQUIRED_MCP_TOOLS = {'filesystem'}
COVERAGE_HEADINGS = [
    'Use this skill when',
    'Workflow',
    'Review output format',
    'Review heuristics',
    'Security and reliability checks (quick)',
    'Agent orchestration',
    'Validation and testing',
    'Outputs',
    'References'
]
REFERENCE_LINKS = [
    {'title': 'OWASP Cheat Sheet Series', 'url': 'https://cheatsheetseries.owasp.org/', 'note': 'Secure defaults and implementation guidance.'},
    {'title': 'OWASP ASVS', 'url': 'https://owasp.org/www-project-application-security-verification-standard/', 'note': 'Application security verification requirements.'},
    {'title': 'NIST SSDF', 'url': 'https://csrc.nist.gov/pubs/sp/800/218/final', 'note': 'Secure software development baseline controls.'},
    {'title': 'Code review best practices', 'url': 'https://google.github.io/eng-practices/review/', 'note': 'Review standards for correctness and maintainability.'}
]


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def references_path() -> Path:
    return skill_root() / 'references' / 'latest-sources.md'


def openai_agent_path() -> Path:
    return skill_root() / 'agents' / 'openai.yaml'


def mcp_dependencies(openai_yaml_path: Path) -> set[str]:
    raw = openai_yaml_path.read_text(encoding='utf-8')
    parsed = yaml.safe_load(raw) or {}
    dependencies = parsed.get('dependencies') or {}
    tools = dependencies.get('tools') or []
    if not isinstance(tools, list):
        return set()

    deps: set[str] = set()
    for tool in tools:
        if not isinstance(tool, dict):
            continue
        dep_type = str(tool.get('type', '')).strip()
        dep_value = str(tool.get('value', '')).strip()
        if dep_type == 'mcp' and dep_value:
            deps.add(dep_value)
    return deps


def summary_payload() -> dict[str, Any]:
    return {
        'skill_name': SKILL_NAME,
        'category': SKILL_CATEGORY,
        'description': SKILL_DESCRIPTION,
        'last_refresh_utc': LAST_REFRESH_UTC,
        'coverage_headings': COVERAGE_HEADINGS,
        'reference_links': REFERENCE_LINKS,
        'references_file': str(references_path()),
        'openai_agent_file': str(openai_agent_path()),
    }


def cmd_summary(as_json: bool) -> int:
    payload = summary_payload()
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    print(f"Skill: {payload['skill_name']}")
    print(f"Category: {payload['category']}")
    print(f"Last refresh (UTC): {payload['last_refresh_utc']}")
    print('Description:')
    print(f"  {payload['description']}")
    print('')
    print('Coverage headings:')
    headings = payload['coverage_headings']
    if headings:
        for item in headings:
            print(f"  - {item}")
    else:
        print('  - (No headings detected; read SKILL.md directly.)')
    print('')
    print('External references:')
    for link in payload['reference_links']:
        print(f"  - {link['title']} -> {link['url']}")
    return 0


def cmd_validate() -> int:
    errors: list[str] = []

    required_dirs = [
        skill_root() / 'assets',
        skill_root() / 'scripts',
        skill_root() / 'references',
        skill_root() / 'agents',
    ]
    for required in required_dirs:
        if not required.is_dir():
            errors.append(f"missing directory: {required}")

    refs = references_path()
    if not refs.is_file():
        errors.append(f"missing references file: {refs}")

    agent_path = openai_agent_path()
    if not agent_path.is_file():
        errors.append(f"missing agent definition: {agent_path}")
    else:
        try:
            deps = mcp_dependencies(agent_path)
            missing = sorted(REQUIRED_MCP_TOOLS - deps)
            if missing:
                errors.append(
                    f"agents/openai.yaml missing required MCP dependencies: {', '.join(missing)}"
                )
        except Exception as exc:  # pragma: no cover - defensive fallback
            errors.append(f'failed to parse agents/openai.yaml: {exc}')

    if errors:
        print('VALIDATION FAILED', file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        return 1

    print('OK: skill helper validation passed')
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f'Helper for {SKILL_NAME} skill workflows')
    parser.add_argument('command', choices=('summary', 'validate'), nargs='?', default='summary')
    parser.add_argument('--json', action='store_true', help='Emit summary as JSON')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == 'validate':
        return cmd_validate()
    return cmd_summary(as_json=args.json)


if __name__ == '__main__':
    raise SystemExit(main())
