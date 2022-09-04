from beanie import init_beanie
import motor.motor_asyncio

from config import settings
from models.meta import Meta
from models.competition import Competition
from models.match import Match
from models.lineup import Lineup
from models.event import Event


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}".format(
            MONGO_USERNAME=settings.MONGO_USERNAME,
            MONGO_PASSWORD=settings.MONGO_PASSWORD,
            MONGO_HOST=settings.MONGO_HOST,
            MONGO_PORT=settings.MONGO_PORT,
            MONGO_DB_NAME=settings.MONGO_DB_NAME)
        , authSource="admin")
    print(client["db_name"])
    print(client.db)
    await init_beanie(database=client.fdp, document_models=[Meta, Competition, Match, Lineup, Event])
