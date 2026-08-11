from __future__ import annotations

from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        env_ignore_empty=True,
    )

    environment: Literal["dev", "test", "prod"] = Field(default="dev")
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(default="INFO")

    host: str = Field(default="127.0.0.1")
    port: int = Field(default=8000, ge=1, le=65535)

    # Enable only when HTTPS is guaranteed end-to-end.
    enable_hsts: bool = Field(default=False)

    # Max request size (bytes) for APIs that accept JSON bodies.
    max_body_bytes: int = Field(default=1_048_576, ge=1, le=50_000_000)


settings = Settings()
