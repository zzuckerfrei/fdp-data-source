from pydantic import BaseSettings

from models.competition import Competition, UpdateCompetition
from models.match import Match, UpdateMatch
from models.lineup import Lineup, UpdateLineup
from models.event import Event, UpdateEvent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    MONGO_HOST = "fdp-mongo"  # localhost (x), fdp-mongo(o), 172.18.0.2 (?) -> todo 환경변수로 받을 것
    MONGO_PORT = 27017
    MONGO_USERNAME = "root"
    MONGO_PASSWORD = "root"

    MONGO_DB_NAME = "fdp"
    MONGO_COL_META = "meta"
    MONGO_COL_COMPETITION = "competition"
    MONGO_COL_MATCH = "match"
    MONGO_COL_LINEUP = "lineup"
    MONGO_COL_EVENT = "event"

    DATA_TYPE = {
        "competition": [Competition, UpdateCompetition],
        "match": [Match, UpdateMatch],
        "lineup": [Lineup, UpdateLineup],
        "event": [Event, UpdateEvent]
    }

    FILE_DIR = {
        "competition": "/Users/smlee/Documents/open-data-master/data/",
        "match": "/Users/smlee/Documents/open-data-master/data/matches",
        "lineup": "/Users/smlee/Documents/open-data-master/data/lineups",
        "event": "/Users/smlee/Documents/open-data-master/data/events"
    }


settings = Settings()
