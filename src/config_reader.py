import pathlib

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_LOCATION = f"{pathlib.Path(__file__).resolve().parent}/.env"


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DATABASE_URL: SecretStr

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_LOCATION,
        env_file_encoding="utf-8"
    )


config = Settings()
