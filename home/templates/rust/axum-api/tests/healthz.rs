use axum::{body::Body, http::Request};
use tower::ServiceExt;

#[tokio::test]
async fn test_healthz() {
    let app = axum_api_template::app();
    let res = app
        .oneshot(Request::builder().uri("/healthz").body(Body::empty()).unwrap())
        .await
        .unwrap();
    assert_eq!(res.status(), 200);
    let request_id = res.headers().get("x-request-id").and_then(|v| v.to_str().ok());
    assert!(request_id.is_some());
}
