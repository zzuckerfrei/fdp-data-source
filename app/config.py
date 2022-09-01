from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    MONGO_USERNAME = "root"
    MONGO_PASSWORD = "root"


settings = Settings()
