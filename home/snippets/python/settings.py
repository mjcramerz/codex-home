from __future__ import annotations

"""Pydantic settings baseline with safe defaults and env prefix.

References: docs/style/python.md
"""

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
    host: str = Field(default="127.0.0.1")
    port: int = Field(default=8000, ge=1, le=65535)
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(default="INFO")

    # Security: keep secrets in env vars, not in code.
    # database_url: str | None = None


settings = Settings()
