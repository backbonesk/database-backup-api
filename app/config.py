from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    APP_NAME: str = "DB Backup API"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()  # type: ignore
