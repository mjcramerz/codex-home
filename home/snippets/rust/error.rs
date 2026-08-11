//! Typed error pattern with safe public messages.
//! References: docs/style/rust.md, docs/security/overview.md

use thiserror::Error;

#[derive(Debug, Error)]
#[non_exhaustive]
pub enum AppError {
    #[error("invalid input: {0}")]
    InvalidInput(String),

    #[error("not found")]
    NotFound,

    #[error("io error: {0}")]
    Io(#[from] std::io::Error),

    #[error("upstream error: {0}")]
    Upstream(String),

    #[error("internal error")]
    Internal,
}

pub type AppResult<T> = Result<T, AppError>;

impl AppError {
    /// Exit codes for CLI apps (sysexits-inspired, but lightweight).
    pub fn exit_code(&self) -> i32 {
        match self {
            AppError::InvalidInput(_) => 2,
            AppError::NotFound => 3,
            AppError::Upstream(_) => 4,
            AppError::Io(_) | AppError::Internal => 1,
        }
    }

    /// A user-facing message that avoids leaking internals.
    pub fn public_message(&self) -> &'static str {
        match self {
            AppError::InvalidInput(_) => "invalid input",
            AppError::NotFound => "not found",
            AppError::Upstream(_) => "upstream error",
            AppError::Io(_) | AppError::Internal => "internal error",
        }
    }
}
