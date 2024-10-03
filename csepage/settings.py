from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URI: str

    model_config = SettingsConfigDict(env_file=".env")


# 설정을 불러옵니다.
settings = Settings()
