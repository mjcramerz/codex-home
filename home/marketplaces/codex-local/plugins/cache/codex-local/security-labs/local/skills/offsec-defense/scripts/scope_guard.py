#!/usr/bin/env python3
"""Validate documented scope for security assessment operations."""
from __future__ import annotations

import argparse
import datetime as dt
import ipaddress
import json
from pathlib import Path
import sys


ALLOWED_OPERATIONS = {
    "port-scan",
    "credential-detection-test",
    "dns-defense-validation",
    "metasploit-lab-validation",
    "wifi-security-assessment",
    "purple-team-replay",
    "reverse-engineering-triage",
}

MAX_SCOPE_FILE_BYTES = 64 * 1024
MAX_TARGET_LENGTH = 128


def parse_utc_timestamp(value: str) -> dt.datetime:
    cleaned = value.strip()
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1] + "+00:00"
    parsed = dt.datetime.fromisoformat(cleaned)
    if parsed.tzinfo is None:
        raise ValueError("expires_utc must include timezone")
    return parsed.astimezone(dt.timezone.utc)


def require_non_empty_str(scope: dict[str, object], key: str) -> str:
    value = scope.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} is required")
    return value.strip()


def validate_scope_file(path: Path) -> None:
    stat = path.stat()
    if stat.st_size <= 0:
        raise ValueError("scope file is empty")
    if stat.st_size > MAX_SCOPE_FILE_BYTES:
        raise ValueError(
            f"scope file exceeds limit ({stat.st_size} bytes > {MAX_SCOPE_FILE_BYTES} bytes)"
        )


def load_scope(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("scope file must contain a JSON object")
    return payload


def parse_networks(
    values: object,
) -> list[ipaddress.IPv4Network | ipaddress.IPv6Network]:
    if not isinstance(values, list) or not values:
        raise ValueError("allowed_networks must be a non-empty list")

    networks: list[ipaddress.IPv4Network | ipaddress.IPv6Network] = []
    for raw in values:
        if not isinstance(raw, str) or not raw.strip():
            raise ValueError("allowed_networks entries must be non-empty strings")
        try:
            networks.append(ipaddress.ip_network(raw.strip(), strict=False))
        except ValueError as exc:
            raise ValueError(f"invalid network entry: {raw}") from exc
    return networks


def target_in_scope(
    target: str, networks: list[ipaddress.IPv4Network | ipaddress.IPv6Network]
) -> bool:
    target = target.strip()
    try:
        host = ipaddress.ip_address(target)
        return any(host in net for net in networks)
    except ValueError:
        pass

    try:
        net = ipaddress.ip_network(target, strict=False)
    except ValueError:
        return False
    return any(net.subnet_of(parent) for parent in networks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate documented assessment scope")
    parser.add_argument("--scope-file", required=True, help="Path to scope JSON file")
    parser.add_argument("--target", required=True, help="IP/CIDR target to validate")
    parser.add_argument("--operation", required=True, help="Requested operation class")
    args = parser.parse_args()

    if args.operation not in ALLOWED_OPERATIONS:
        print(f"ERROR: unsupported operation: {args.operation}", file=sys.stderr)
        return 2

    target = args.target.strip()
    if not target or len(target) > MAX_TARGET_LENGTH:
        print(
            f"ERROR: target must be a non-empty IP/CIDR value <= {MAX_TARGET_LENGTH} chars",
            file=sys.stderr,
        )
        return 2

    scope_path = Path(args.scope_file)
    if not scope_path.exists() or not scope_path.is_file():
        print(f"ERROR: scope file not found: {scope_path}", file=sys.stderr)
        return 2

    try:
        validate_scope_file(scope_path)
        scope = load_scope(scope_path)
        scope_id = require_non_empty_str(scope, "scope_id")
        owner = require_non_empty_str(scope, "owner")

        if scope.get("lab_only") is not True:
            raise ValueError("lab_only must be true")

        expires_raw = require_non_empty_str(scope, "expires_utc")
        expires_utc = parse_utc_timestamp(expires_raw)
        if expires_utc <= dt.datetime.now(dt.timezone.utc):
            raise ValueError("scope is expired")

        networks = parse_networks(scope.get("allowed_networks"))
        allowed_ops = scope.get("allowed_operations")
        if not isinstance(allowed_ops, list) or not allowed_ops:
            raise ValueError("allowed_operations must be a non-empty list")
        if not all(
            isinstance(item, str) and item in ALLOWED_OPERATIONS for item in allowed_ops
        ):
            raise ValueError("allowed_operations must be a list of supported operation names")
        if args.operation not in allowed_ops:
            raise ValueError(f"operation not in scope: {args.operation}")

        if not target_in_scope(target, networks):
            raise ValueError(f"target out of scope: {target}")
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "status": "validated",
                "target": target,
                "operation": args.operation,
                "scope_id": scope_id,
                "owner": owner,
                "expires_utc": expires_raw,
                "scope_file": str(scope_path),
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
