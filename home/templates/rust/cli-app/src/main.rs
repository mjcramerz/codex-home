#![forbid(unsafe_code)]

use clap::Parser;

mod cli;
mod error;
mod tracing_init;

use crate::cli::Args;
use crate::error::AppResult;

fn run(_args: &Args) -> AppResult<()> {
    tracing::info!("hello from rust_cli_template");
    Ok(())
}

fn main() -> std::process::ExitCode {
    let args = Args::parse();
    std::env::set_var("LOG_FORMAT", args.log_format.as_str());
    tracing_init::init_tracing(args.verbose, args.log_format);

    match run(&args) {
        Ok(()) => std::process::ExitCode::SUCCESS,
        Err(err) => {
            tracing::error!(error = %err, "fatal");
            eprintln!("{}", err.public_message());
            std::process::ExitCode::from(err.exit_code())
        }
    }
}
