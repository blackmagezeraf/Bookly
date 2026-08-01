"""API Configurations."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Bookly API settings."""

    VERSION: str = ""
    DATABASE_PROTOCOL: str = ""
    DATABASE_USERNAME: str = ""
    DATABASE_PASSWORD: str = ""
    DATABASE_HOST: str = ""
    DATABASE_PORT: int = ""
    DATABASE_NAME: str = ""

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    RELOAD: bool = True
    RELOAD_DIRS: list[str] = [""]
    RELOAD_INCLUDES: list[str] = [""]

    model_config = SettingsConfigDict(env_file="development.env", extra="ignore")

    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DATABASE_PROTOCOL}://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"


Config = Settings()
