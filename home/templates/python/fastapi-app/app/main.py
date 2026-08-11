from __future__ import annotations

import logging
import os
import time
import uuid
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .security_headers import SecurityHeadersConfig, install_security_headers
from .settings import settings
from .logging_ import configure_logging, request_id_var

# Apply settings-driven defaults for logging.
os.environ.setdefault("LOG_LEVEL", settings.log_level)
configure_logging()
log = logging.getLogger("app")

docs_enabled = settings.environment != "prod"
app = FastAPI(
    title="FastAPI App",
    version="0.1.0",
    docs_url="/docs" if docs_enabled else None,
    redoc_url="/redoc" if docs_enabled else None,
    openapi_url="/openapi.json" if docs_enabled else None,
)

install_security_headers(
    app,
    config=SecurityHeadersConfig(
        content_security_policy="default-src 'none'; frame-ancestors 'none'; base-uri 'none'",
        strict_transport_security=(
            "max-age=31536000; includeSubDomains" if settings.enable_hsts else None
        ),
    ),
)


@app.middleware("http")
async def add_request_id_and_timing(request: Request, call_next):
    start = time.perf_counter()

    content_length = request.headers.get("content-length")
    if content_length:
        try:
            size = int(content_length)
        except ValueError:
            return JSONResponse(status_code=400, content={"detail": "invalid content-length"})
        if size > settings.max_body_bytes:
            return JSONResponse(status_code=413, content={"detail": "request too large"})

    # Accept a bounded request-id header if provided; otherwise generate one.
    req_id = request.headers.get("x-request-id")
    if not req_id or len(req_id) > 128 or not req_id.isascii():
        req_id = uuid.uuid4().hex

    token = request_id_var.set(req_id)
    try:
        response = await call_next(request)
    finally:
        request_id_var.reset(token)

    dur_ms = int((time.perf_counter() - start) * 1000)
    response.headers["x-request-id"] = req_id
    response.headers["x-response-time-ms"] = str(dur_ms)
    return response


@app.get("/healthz")
async def healthz() -> dict[str, Any]:
    payload: dict[str, Any] = {"status": "ok"}
    if settings.environment != "prod":
        payload["env"] = settings.environment
    return payload


@app.exception_handler(Exception)
async def unhandled_exc_handler(request: Request, exc: Exception):
    # Avoid leaking internal errors to clients.
    log.exception("unhandled exception")
    return JSONResponse(status_code=500, content={"detail": "internal error"})
