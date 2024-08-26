from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    user: str
    password: str
    db: str

    class Config:
        env_prefix = "postgres_"


class RedisSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = "redis_"


class DostavistaSettings(BaseSettings):
    token: str

    class Config:
        env_prefix = "dostavista_"


class Settings(BaseSettings):
    debug: bool

    database: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    dostavista: DostavistaSettings = DostavistaSettings()


settings = Settings()
