//! Tracing initialization with env filter and optional JSON output.
//! References: docs/style/rust.md

use tracing_subscriber::util::SubscriberInitExt;
use tracing_subscriber::{fmt, EnvFilter};

/// Initialize `tracing` with a sane default filter and optional JSON formatting.
///
/// - Filter: `RUST_LOG` if set, otherwise `default_filter`.
/// - Format: `LOG_FORMAT=json` (requires `tracing-subscriber` with the `json` feature).
pub fn init_tracing(default_filter: &str) {
    let filter = match EnvFilter::try_from_default_env() {
        Ok(filter) => filter,
        Err(_) => {
            let fallback = std::env::var("LOG_LEVEL").unwrap_or_else(|_| default_filter.to_string());
            EnvFilter::new(fallback)
        }
    };
    let use_json = std::env::var("LOG_FORMAT")
        .ok()
        .is_some_and(|v| v.eq_ignore_ascii_case("json"));

    let fmt_builder = fmt()
        .with_env_filter(filter)
        .with_target(false)
        .with_level(true);

    #[cfg(feature = "json")]
    let fmt_builder = if use_json { fmt_builder.json() } else { fmt_builder.compact() };

    #[cfg(not(feature = "json"))]
    let fmt_builder = {
        let _ = use_json; // suppress unused warnings when json feature is off
        fmt_builder.compact()
    };

    // `try_init` avoids panics in tests when tracing is initialized multiple times.
    let _ = fmt_builder.try_init();
}
