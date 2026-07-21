"""API Configurations."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Bookly API settings."""

    VERSION: str = ""
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file="development.env", extra="ignore"
    )


Config = Settings()
