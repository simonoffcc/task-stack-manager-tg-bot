import logging
from dataclasses import dataclass
from os import getenv


@dataclass
class DatabaseConfig:
    database_system: str = 'sqlite'
    driver: str = 'aiosqlite'
    engine_url: str = 'sqlite+aiosqlite:///db.sqlite3'

    def build_connection_str(self) -> str:
        return self.engine_url


@dataclass
class RedisConfig:
    db: int = int(getenv('REDIS_DATABASE', 1))
    host: str = getenv('REDIS_HOST', 'redis')
    port: int = int(getenv('REDIS_PORT', 6379))
    passwd: str | None = getenv('REDIS_PASSWORD')
    username: str | None = getenv('REDIS_USERNAME')
    state_ttl: int | None = getenv('REDIS_TTL_STATE', None)
    data_ttl: int | None = getenv('REDIS_TTL_DATA', None)


@dataclass
class BotConfig:
    token: str = getenv('BOT_TOKEN')


@dataclass
class Configuration:
    debug = bool(getenv('DEBUG', 1))
    logging_level = int(getenv('LOGGING_LEVEL', logging.INFO))

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()


conf = Configuration()
