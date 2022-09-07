from pymongo import MongoClient

from config import settings


def get_client():
    return MongoClient(host=settings.MONGO_HOST,
                       port=settings.MONGO_PORT,
                       username=settings.MONGO_USERNAME,
                       password=settings.MONGO_PASSWORD)
