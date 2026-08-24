#!/usr/bin/env python3
"""Validate documented scope for mobile and wireless defense operations."""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import re
import sys


ALLOWED_OPERATIONS = {
    "wifi-defense-assessment",
    "nethunter-build-validation",
    "rooted-device-risk-check",
    "badusb-defense-drill",
}

MAX_SCOPE_FILE_BYTES = 64 * 1024
MAX_DEVICE_ID_LENGTH = 64
DEVICE_ID_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")


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


def validate_device_id(value: str) -> str:
    device_id = value.strip()
    if not device_id:
        raise ValueError("device-id must be non-empty")
    if len(device_id) > MAX_DEVICE_ID_LENGTH:
        raise ValueError(
            f"device-id exceeds max length ({MAX_DEVICE_ID_LENGTH} characters)"
        )
    if not DEVICE_ID_PATTERN.fullmatch(device_id):
        raise ValueError(
            "device-id contains unsupported characters (allowed: A-Z, a-z, 0-9, . _ : -)"
        )
    return device_id


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate mobile and wireless scope")
    parser.add_argument("--scope-file", required=True)
    parser.add_argument("--operation", required=True)
    parser.add_argument("--device-id", required=True)
    args = parser.parse_args()

    if args.operation not in ALLOWED_OPERATIONS:
        print(f"ERROR: unsupported operation: {args.operation}", file=sys.stderr)
        return 2

    try:
        device_id = validate_device_id(args.device_id)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    scope_path = Path(args.scope_file)
    if not scope_path.exists() or not scope_path.is_file():
        print(f"ERROR: scope file not found: {scope_path}", file=sys.stderr)
        return 2

    try:
        validate_scope_file(scope_path)
        scope = json.loads(scope_path.read_text(encoding="utf-8"))
        if not isinstance(scope, dict):
            raise ValueError("scope must be a JSON object")
        scope_id = require_non_empty_str(scope, "scope_id")
        owner = require_non_empty_str(scope, "owner")
        if scope.get("lab_only") is not True:
            raise ValueError("lab_only must be true")
        expires_raw = require_non_empty_str(scope, "expires_utc")
        expires_utc = parse_utc_timestamp(expires_raw)
        if expires_utc <= dt.datetime.now(dt.timezone.utc):
            raise ValueError("scope is expired")

        allowed_ops = scope.get("allowed_operations")
        if not isinstance(allowed_ops, list) or not allowed_ops:
            raise ValueError("allowed_operations must be a non-empty list")
        if not all(
            isinstance(op, str) and op in ALLOWED_OPERATIONS for op in allowed_ops
        ):
            raise ValueError("allowed_operations contains unsupported entries")
        if args.operation not in allowed_ops:
            raise ValueError(f"operation not in scope: {args.operation}")

        devices = scope.get("allowed_devices")
        if not isinstance(devices, list) or not devices:
            raise ValueError("allowed_devices must be a non-empty list")
        normalized_devices: set[str] = set()
        for raw in devices:
            if not isinstance(raw, str):
                raise ValueError("allowed_devices entries must be strings")
            normalized_devices.add(validate_device_id(raw))
        if device_id not in normalized_devices:
            raise ValueError(f"device not in scope: {device_id}")
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "status": "validated",
                "operation": args.operation,
                "device_id": device_id,
                "scope_id": scope_id,
                "owner": owner,
                "expires_utc": expires_raw,
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
