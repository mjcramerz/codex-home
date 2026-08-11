//! Axum timeout layers with conservative defaults.
//! References: docs/security/overview.md, docs/perf/overview.md

use axum::http::StatusCode;
use axum::Router;
use std::time::Duration;
use tower::ServiceBuilder;
use tower_http::limit::RequestBodyLimitLayer;
use tower_http::timeout::{RequestBodyTimeoutLayer, TimeoutLayer};

/// Apply conservative HTTP timeouts to an Axum `Router`.
///
/// Notes:
/// - `RequestBodyTimeoutLayer` mitigates slowloris-style request bodies.
/// - `TimeoutLayer` bounds total request processing time and (by default) returns 408 on timeout.
pub fn apply_timeouts(router: Router) -> Router {
    let request_timeout = Duration::from_secs(30);
    let body_chunk_timeout = Duration::from_secs(10);
    let max_body_bytes: usize = 1 * 1024 * 1024;

    router.layer(
        ServiceBuilder::new()
            .layer(RequestBodyLimitLayer::new(max_body_bytes))
            .layer(RequestBodyTimeoutLayer::new(body_chunk_timeout))
            .layer(TimeoutLayer::with_status_code(
                StatusCode::REQUEST_TIMEOUT,
                request_timeout,
            )),
    )
}
