from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz() -> None:
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

    # Middleware adds basic observability + correlation IDs.
    assert "x-request-id" in r.headers
    assert r.headers["x-request-id"]
    assert r.headers.get("x-response-time-ms", "").isdigit()

    # Conservative security headers (safe for JSON APIs).
    assert r.headers.get("x-content-type-options") == "nosniff"
    assert r.headers.get("x-frame-options") == "DENY"
    assert r.headers.get("referrer-policy") == "no-referrer"
    assert r.headers.get("permissions-policy") == "geolocation=(), microphone=(), camera=(), interest-cohort=()"
    assert r.headers.get("cross-origin-opener-policy") == "same-origin"
    assert r.headers.get("cross-origin-resource-policy") == "same-origin"
