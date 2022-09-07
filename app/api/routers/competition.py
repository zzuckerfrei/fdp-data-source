# from typing import Union
# from pprint import pprint
#
# from fastapi import APIRouter, Depends
# from pymongo import MongoClient
# from bson.objectid import ObjectId
#
# from .. import dependencies as deps
# from config import settings
#
# router = APIRouter()
#
#
# # 0. create collection if not exists
# # 1. get file list, return file_count & file_list
# @router.get("/dir_info")
# def get_dir_info():
#     pass
#
#
# # 2. insert
# @router.post("/insert")
# def insert_one(client: MongoClient = Depends(deps.get_client)):
#     collection = client.get_database(settings.MONGO_DB_NAME).get_collection(settings.MONGO_COL_COMPETITION)
#     collection.insert_one()
#     return 1
#
# ## example
# @app.post("/insert_one", response_model=ResEvent)
# async def insert_one(event_one: ReqEvent):
#     collection.insert_one(event_one.dict())
#     return event_one
#
#
# # 3. find
# @router.get("/find")
# def find_all(client: MongoClient = Depends(deps.get_client)):
#     collection = client.get_database(settings.MONGO_DB_NAME).get_collection(settings.MONGO_COL_COMPETITION)
#     session = client.start_session()
#     find_json = collection.find(session=session)
#     pprint(find_json)
#
#     return find_json
#
# # 4. update meta
