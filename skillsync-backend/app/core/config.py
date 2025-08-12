from pydantic import BaseSettings
class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str
    USE_FAISS: bool = False
    class Config:
        env_file = ".env"
settings = Settings()
