#!/usr/bin/env python3
"""Read and render configuration as TOML, never as JSON Schema documentation.

Schema validation belongs to the build tooling. This module only handles TOML
syntax, explicit tables/arrays of tables, and the no-schema-dump file contract.
It does not invent settings or choose runtime values.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import re
import tomllib
from typing import Any, Mapping, Sequence

# These are documentation artifacts, not Codex settings. Restrict the scan to
# comments so legitimate settings named `type` or `description` remain valid.
_SCHEMA_COMMENT = re.compile(
    r'^\s*#\s*(?:'
    r'(?:BEGIN|END) GENERATED SUPPORTED-KEY REFERENCE\b|'
    r'schema-(?:definition|entry|variant|options|finite-option|example):|'
    r':schema\b|'
    r'\#/(?:definitions|\$defs|properties)/'
    r')',
    re.MULTILINE,
)
_SCHEMA_ROOT_KEYS = frozenset({
    '$schema', '$ref', '$defs', 'definitions', 'properties',
    'additionalProperties', 'allOf', 'anyOf', 'oneOf',
})
_BARE_KEY = re.compile(r'^[A-Za-z0-9_-]+$')


def _comments(text: str):
    """Yield actual TOML comments, excluding comment-like content in strings.

TOML is parsed before this scan. Runs of up to five closing quotes in multiline
strings and escaped quotes in basic strings therefore have their standard forms.
"""
    index = 0
    quote = None
    multiline = False
    while index < len(text):
        char = text[index]
        if quote is None:
            if char == '#':
                end = text.find('\n', index)
                if end < 0:
                    end = len(text)
                yield index, text[index:end]
                index = end
                continue
            if char in ('"', "'"):
                quote = char
                multiline = text.startswith(char * 3, index)
                index += 3 if multiline else 1
                continue
        elif quote == '"' and char == '\\':
            index += 2
            continue
        elif char == quote:
            if not multiline:
                quote = None
                index += 1
                continue
            end = index
            while end < len(text) and text[end] == quote:
                end += 1
            if end - index >= 3:
                quote = None
            index = end
            continue
        index += 1


def clean_loads(text: str, label: str = 'configuration') -> dict[str, Any]:
    """Parse TOML and reject accidentally embedded schema/coverage material."""
    data = tomllib.loads(text)
    for offset, comment in _comments(text):
        if _SCHEMA_COMMENT.search(comment):
            line = text.count('\n', 0, offset) + 1
            raise ValueError(f'{label}:{line}: schema metadata belongs in generate/reports/, not TOML')
    bad = sorted(_SCHEMA_ROOT_KEYS.intersection(data))
    if bad:
        raise ValueError(f'{label}: JSON Schema keywords are not configuration keys: {bad}')
    return data


def clean_load(path: Path) -> dict[str, Any]:
    return clean_loads(path.read_text(encoding='utf-8'), str(path))


def key(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError('TOML keys must be strings')
    return value if _BARE_KEY.fullmatch(value) else json.dumps(value, ensure_ascii=False)


def table_path(parts: Sequence[str]) -> str:
    return '.'.join(key(part) for part in parts)


def literal(value: Any, *, multiline: bool = True) -> str:
    if isinstance(value, str):
        if multiline and '\n' in value:
            # Encode each line separately so a literal backslash-n is NOT turned
            # into a newline. The opening newline is trimmed by TOML, not data.
            body = '\n'.join(json.dumps(part, ensure_ascii=False)[1:-1] for part in value.split('\n'))
            return '"""\n' + body + '"""'
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError('non-finite floats are not configuration examples')
        return repr(value)
    if isinstance(value, list):
        return '[' + ', '.join(literal(item, multiline=False) for item in value) + ']'
    if isinstance(value, Mapping):
        # Used only for a mixed array value. Regular mappings are real tables.
        return '{ ' + ', '.join(f'{key(k)} = {literal(v, multiline=False)}' for k, v in value.items()) + ' }'
    raise TypeError(f'unsupported TOML value: {type(value).__name__}')


def render_mapping(
    lines: list[str],
    value: Mapping[str, Any],
    *,
    path: tuple[str, ...] = (),
    comments: Mapping[tuple[str, ...], Sequence[str]] | None = None,
) -> None:
    """Emit scalars, then [tables] and [[arrays.of.tables]], in TOML scope order."""
    notes = comments or {}
    nested: list[tuple[str, Any]] = []
    for name, child in value.items():
        child_path = path + (name,)
        if isinstance(child, Mapping) or (
            isinstance(child, list) and child and all(isinstance(item, Mapping) for item in child)
        ):
            nested.append((name, child))
            continue
        lines.extend(notes.get(child_path, ()))
        rendered = literal(child)
        if isinstance(child, list) and child and '\n' not in rendered and len(rendered) > 100:
            lines.append(f'{key(name)} = [')
            lines.extend(f'  {literal(item, multiline=False)},' for item in child)
            lines.append(']')
        else:
            lines.append(f'{key(name)} = {rendered}')
    for name, child in nested:
        child_path = path + (name,)
        items = [child] if isinstance(child, Mapping) else child
        for item in items:
            if lines and lines[-1] != '':
                lines.append('')
            lines.extend(notes.get(child_path, ()))
            marker = '[' if isinstance(child, Mapping) else '[['
            close = ']' if isinstance(child, Mapping) else ']]'
            lines.append(marker + table_path(child_path) + close)
            render_mapping(lines, item, path=child_path, comments=notes)


def dumps(
    value: Mapping[str, Any],
    *,
    header: Sequence[str] = (),
    comments: Mapping[tuple[str, ...], Sequence[str]] | None = None,
) -> str:
    lines = list(header)
    if lines:
        lines.append('')
    render_mapping(lines, value, comments=comments)
    result = '\n'.join(lines).rstrip() + '\n'
    if clean_loads(result) != value:
        raise ValueError('rendering changed TOML values')
    return result
