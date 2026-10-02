use crate::cli::LogFormat;
use tracing_subscriber::util::SubscriberInitExt;
use tracing_subscriber::{fmt, EnvFilter};

pub fn init_tracing(verbose: u8, log_format: LogFormat) {
    let default_filter = match verbose {
        0 => "info",
        1 => "debug",
        _ => "trace",
    };

    let filter = match EnvFilter::try_from_default_env() {
        Ok(filter) => filter,
        Err(_) => {
            let fallback = std::env::var("LOG_LEVEL").unwrap_or_else(|_| default_filter.to_string());
            EnvFilter::new(fallback)
        }
    };

    let fmt_builder = fmt()
        .with_env_filter(filter)
        .with_target(false)
        .with_level(true);

    let fmt_builder = match log_format {
        LogFormat::Compact => fmt_builder.compact(),
        LogFormat::Json => fmt_builder.json(),
    };

    let _ = fmt_builder.try_init();
}
