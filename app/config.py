from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    MONGO_USERNAME = "root"
    MONGO_PASSWORD = "root"

    MONGO_DB_NAME = "fdp"
    MONGO_COL_META = "meta"
    MONGO_COL_COMPETITION = "competition"
    MONGO_COL_MATCH = "match"
    MONGO_COL_LINEUP = "lineup"
    MONGO_COL_EVENT = "event"


settings = Settings()
