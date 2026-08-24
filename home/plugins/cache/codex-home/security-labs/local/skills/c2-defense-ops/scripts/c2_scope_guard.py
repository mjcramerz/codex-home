#!/usr/bin/env python3
"""Validate documented scope for C2 defense operations."""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import re
import sys


ALLOWED_OPERATIONS = {
    "c2-detection-replay",
    "redirector-validation",
    "reverse-shell-detection",
    "credential-access-detection",
}

MAX_SCOPE_FILE_BYTES = 64 * 1024
MAX_TARGET_LABEL_LENGTH = 80
TARGET_LABEL_PATTERN = re.compile(r"^[A-Za-z0-9._:@/-]+$")


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


def validate_target_label(value: str) -> str:
    label = value.strip()
    if not label:
        raise ValueError("target-label must be non-empty")
    if len(label) > MAX_TARGET_LABEL_LENGTH:
        raise ValueError(
            f"target-label exceeds max length ({MAX_TARGET_LABEL_LENGTH} characters)"
        )
    if not TARGET_LABEL_PATTERN.fullmatch(label):
        raise ValueError(
            "target-label contains unsupported characters (allowed: A-Z, a-z, 0-9, . _ : @ / -)"
        )
    return label


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate C2 defense scope")
    parser.add_argument("--scope-file", required=True)
    parser.add_argument("--operation", required=True)
    parser.add_argument("--target-label", required=True)
    args = parser.parse_args()

    if args.operation not in ALLOWED_OPERATIONS:
        print(f"ERROR: unsupported operation: {args.operation}", file=sys.stderr)
        return 2

    try:
        target_label = validate_target_label(args.target_label)
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

        allowed = scope.get("allowed_operations")
        if not isinstance(allowed, list) or not allowed:
            raise ValueError("allowed_operations must be a non-empty list")
        if not all(isinstance(item, str) and item in ALLOWED_OPERATIONS for item in allowed):
            raise ValueError("allowed_operations must contain only supported operation names")
        if args.operation not in allowed:
            raise ValueError(f"operation not in scope: {args.operation}")

        authorized_labels = scope.get("allowed_target_labels")
        if not isinstance(authorized_labels, list) or not authorized_labels:
            raise ValueError("allowed_target_labels must be a non-empty list")
        if not all(
            isinstance(item, str)
            and item.strip()
            and len(item.strip()) <= MAX_TARGET_LABEL_LENGTH
            and TARGET_LABEL_PATTERN.fullmatch(item.strip())
            for item in authorized_labels
        ):
            raise ValueError("allowed_target_labels contains invalid entries")
        if target_label not in {item.strip() for item in authorized_labels}:
            raise ValueError(f"target-label not in scope: {target_label}")
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "status": "validated",
                "operation": args.operation,
                "target_label": target_label,
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
