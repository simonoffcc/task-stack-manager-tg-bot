import logging
from dataclasses import dataclass
from os import getenv


@dataclass
class DatabaseConfig:
    """
    name: str | None = getenv('POSTGRES_DATABASE', 'template1')
    user: str | None = getenv('POSTGRES_USER', 'postgres')
    passwd: str | None = getenv('POSTGRES_PASSWORD',)
    port: int = int(getenv('POSTGRES_PORT', 5432))
    host: str = getenv('POSTGRES_HOST', 'localhost')

    driver: str = 'asyncpg'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)
    """
    engine: str = getenv('DB_STR', 'sqlite+aiosqlite:///db.sqlite3')
    echo: bool = getenv('DB_ECHO', True)

    def build_connection_str(self) -> str:
        return self.engine


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
