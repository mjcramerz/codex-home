from __future__ import annotations

from dataclasses import dataclass

from fastapi import FastAPI
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send


@dataclass(frozen=True)
class SecurityHeadersConfig:
    # Conservative defaults that are safe for JSON APIs.
    x_content_type_options: str = "nosniff"
    x_frame_options: str = "DENY"
    referrer_policy: str = "no-referrer"
    permissions_policy: str = "geolocation=(), microphone=(), camera=(), interest-cohort=()"

    # Strict CSP for APIs that never serve HTML. Swagger UI will break unless skipped.
    # Example: "default-src 'none'; frame-ancestors 'none'; base-uri 'none'"
    content_security_policy: str | None = None

    # Only set HSTS when you are certain HTTPS is guaranteed end-to-end.
    # Example: "max-age=31536000; includeSubDomains"
    strict_transport_security: str | None = None

    # Cross-origin isolation headers (can be restrictive; set to None to disable).
    cross_origin_opener_policy: str | None = "same-origin"
    cross_origin_resource_policy: str | None = "same-origin"

    csp_skip_paths: tuple[str, ...] = ("/docs", "/redoc", "/openapi.json")


class SecurityHeadersMiddleware:
    def __init__(self, app: ASGIApp, *, config: SecurityHeadersConfig | None = None) -> None:
        self._app = app
        self._cfg = config or SecurityHeadersConfig()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self._app(scope, receive, send)
            return

        path = scope.get("path") or ""
        cfg = self._cfg

        def should_set_hsts() -> bool:
            return scope.get("scheme") == "https"

        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)

                if headers.get("x-content-type-options") is None:
                    headers["x-content-type-options"] = cfg.x_content_type_options
                if headers.get("x-frame-options") is None:
                    headers["x-frame-options"] = cfg.x_frame_options
                if headers.get("referrer-policy") is None:
                    headers["referrer-policy"] = cfg.referrer_policy
                if headers.get("permissions-policy") is None:
                    headers["permissions-policy"] = cfg.permissions_policy

                if (
                    cfg.cross_origin_opener_policy is not None
                    and headers.get("cross-origin-opener-policy") is None
                ):
                    headers["cross-origin-opener-policy"] = cfg.cross_origin_opener_policy
                if (
                    cfg.cross_origin_resource_policy is not None
                    and headers.get("cross-origin-resource-policy") is None
                ):
                    headers["cross-origin-resource-policy"] = cfg.cross_origin_resource_policy

                if (
                    cfg.strict_transport_security is not None
                    and should_set_hsts()
                    and headers.get("strict-transport-security") is None
                ):
                    headers["strict-transport-security"] = cfg.strict_transport_security

                if (
                    cfg.content_security_policy is not None
                    and path not in cfg.csp_skip_paths
                    and headers.get("content-security-policy") is None
                ):
                    headers["content-security-policy"] = cfg.content_security_policy

            await send(message)

        await self._app(scope, receive, send_wrapper)


def install_security_headers(app: FastAPI, *, config: SecurityHeadersConfig | None = None) -> None:
    app.add_middleware(SecurityHeadersMiddleware, config=config)
