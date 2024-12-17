from dotenv import load_dotenv
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    # DB settings
    DB_USER: str = "user"
    DB_PASSWORD: str = "pass"
    DB_NAME: str = "db"
    DB_HOST: str = "localhost"
    DB_PORT: int = 27017
    DB_COLLECTION: str = "collection"

    @computed_field
    def dsn(self) -> str:
        return f"mongodb://{self.DB_HOST}:{self.DB_PORT}/"


config = Config()
