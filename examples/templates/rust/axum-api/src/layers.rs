use axum::http::{HeaderName, Request, StatusCode};
use axum::Router;
use std::time::Duration;
use tower::ServiceBuilder;
use tower_http::limit::RequestBodyLimitLayer;
use tower_http::request_id::{MakeRequestUuid, PropagateRequestIdLayer, SetRequestIdLayer};
use tower_http::timeout::TimeoutLayer;
use tower_http::trace::TraceLayer;

pub fn apply(router: Router) -> Router {
    fn env_u64(name: &str, default: u64) -> u64 {
        std::env::var(name)
            .ok()
            .and_then(|v| v.parse().ok())
            .unwrap_or(default)
    }

    fn env_usize(name: &str, default: usize) -> usize {
        std::env::var(name)
            .ok()
            .and_then(|v| v.parse().ok())
            .unwrap_or(default)
    }

    let max_request_bytes = env_usize("APP_MAX_BODY_BYTES", 1 * 1024 * 1024);
    let request_timeout = Duration::from_secs(env_u64("APP_REQUEST_TIMEOUT_SECS", 30));

    let request_id_header = HeaderName::from_static("x-request-id");

    router.layer(
        ServiceBuilder::new()
            .layer(RequestBodyLimitLayer::new(max_request_bytes))
            .layer(TimeoutLayer::with_status_code(
                StatusCode::REQUEST_TIMEOUT,
                request_timeout,
            ))
            .layer(SetRequestIdLayer::new(request_id_header.clone(), MakeRequestUuid))
            .layer(PropagateRequestIdLayer::new(request_id_header))
            .layer(
                TraceLayer::new_for_http().make_span_with(|request: &Request<_>| {
                    let request_id = request
                        .headers()
                        .get("x-request-id")
                        .and_then(|v| v.to_str().ok())
                        .unwrap_or("-");
                    tracing::info_span!(
                        "request",
                        method = %request.method(),
                        uri = %request.uri(),
                        request_id = %request_id,
                    )
                }),
            ),
    )
}
