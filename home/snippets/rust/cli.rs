//! Minimal CLI parsing snippet with log-format support.
//! References: docs/style/rust.md

use clap::{Parser, ValueEnum};

#[derive(Copy, Clone, Debug, ValueEnum)]
pub enum LogFormat {
    Compact,
    Json,
}

impl LogFormat {
    pub fn as_str(self) -> &'static str {
        match self {
            LogFormat::Compact => "compact",
            LogFormat::Json => "json",
        }
    }
}

#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None)]
pub struct Args {
    /// Increase verbosity (-v, -vv). Overrides RUST_LOG defaults in your tracing init.
    #[arg(short, long, action = clap::ArgAction::Count)]
    pub verbose: u8,

    /// Log format (Json requires `tracing-subscriber` with the `json` feature).
    #[arg(long, value_enum, default_value_t = LogFormat::Compact)]
    pub log_format: LogFormat,
}
