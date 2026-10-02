use thiserror::Error;

#[derive(Debug, Error)]
#[non_exhaustive]
pub enum AppError {
    #[error("invalid input: {0}")]
    InvalidInput(String),

    #[error(transparent)]
    Io(#[from] std::io::Error),

    #[error("internal error")]
    Internal,
}

pub type AppResult<T> = Result<T, AppError>;

impl AppError {
    pub fn exit_code(&self) -> u8 {
        match self {
            AppError::InvalidInput(_) => 2,
            AppError::Io(_) | AppError::Internal => 1,
        }
    }

    /// A user-facing message that avoids leaking internals.
    pub fn public_message(&self) -> &'static str {
        match self {
            AppError::InvalidInput(_) => "invalid input",
            AppError::Io(_) | AppError::Internal => "internal error",
        }
    }
}
