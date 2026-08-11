from __future__ import annotations

"""Hardened HTTPX client defaults (timeouts, limits, safe redirects).

References: docs/security/overview.md, Use skill appsec-hardening.
"""

from collections.abc import Mapping

import httpx

DEFAULT_TIMEOUT = httpx.Timeout(connect=5.0, read=15.0, write=15.0, pool=5.0)
DEFAULT_LIMITS = httpx.Limits(max_connections=20, max_keepalive_connections=10, keepalive_expiry=30.0)
DEFAULT_HEADERS: Mapping[str, str] = {"user-agent": "codex-http-client/0.1"}


def build_client(
    *,
    timeout: httpx.Timeout = DEFAULT_TIMEOUT,
    limits: httpx.Limits = DEFAULT_LIMITS,
    headers: Mapping[str, str] | None = None,
    trust_env: bool = False,
) -> httpx.Client:
    """Build a hardened `httpx.Client`.

    Security notes:
    - `follow_redirects=False` avoids SSRF "bounce" surprises.
    - `trust_env=False` ignores proxy env vars by default; set True only when you control the environment.
    """

    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}

    return httpx.Client(
        timeout=timeout,
        limits=limits,
        headers=merged_headers,
        follow_redirects=False,
        trust_env=trust_env,
    )


def build_async_client(
    *,
    timeout: httpx.Timeout = DEFAULT_TIMEOUT,
    limits: httpx.Limits = DEFAULT_LIMITS,
    headers: Mapping[str, str] | None = None,
    trust_env: bool = False,
) -> httpx.AsyncClient:
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}

    return httpx.AsyncClient(
        timeout=timeout,
        limits=limits,
        headers=merged_headers,
        follow_redirects=False,
        trust_env=trust_env,
    )
