#![forbid(unsafe_code)]

use axum::{routing::get, Json, Router};
use serde::Serialize;

mod layers;

#[derive(Debug, Serialize)]
struct Healthz {
    status: &'static str,
    version: &'static str,
}

async fn healthz() -> Json<Healthz> {
    Json(Healthz {
        status: "ok",
        version: env!("CARGO_PKG_VERSION"),
    })
}

/// Build the full application router (routes + middleware layers).
pub fn app() -> Router {
    let router = Router::new().route("/healthz", get(healthz));
    layers::apply(router)
}

/// Backwards-compatible alias.
pub fn router() -> Router {
    app()
}
