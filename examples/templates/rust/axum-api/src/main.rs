#![forbid(unsafe_code)]

use std::net::SocketAddr;
use tokio::net::TcpListener;
use tracing::info;

mod tracing_init;

async fn shutdown_signal() {
    // Ctrl-C
    let ctrl_c = async {
        let _ = tokio::signal::ctrl_c().await;
    };

    // SIGTERM (Unix only)
    #[cfg(unix)]
    let terminate = async {
        use tokio::signal::unix::{signal, SignalKind};
        let mut sigterm = signal(SignalKind::terminate()).expect("install SIGTERM handler");
        sigterm.recv().await;
    };

    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();

    tokio::select! {
        _ = ctrl_c => {},
        _ = terminate => {},
    }
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    tracing_init::init_tracing("info,axum_api_template=debug");

    let app = axum_api_template::app();

    let addr_str = std::env::var("BIND_ADDR").unwrap_or_else(|_| {
        std::env::var("PORT")
            .ok()
            .map(|port| format!("0.0.0.0:{port}"))
            .unwrap_or_else(|| "127.0.0.1:3000".to_string())
    });
    let addr: SocketAddr = addr_str.parse()?;

    let listener = TcpListener::bind(addr).await?;
    info!(%addr, "listening");

    axum::serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await?;
    Ok(())
}
