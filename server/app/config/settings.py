from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "server"
    port: int = 8000
    host: str = "0.0.0.0"
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
