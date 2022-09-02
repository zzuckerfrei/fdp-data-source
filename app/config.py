from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    MONGO_USERNAME = "root"
    MONGO_PASSWORD = "root"

    API_V1_STR: str = "/api/v1"


settings = Settings()
