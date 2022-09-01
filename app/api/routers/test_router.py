from fastapi import APIRouter, Depends
from typing import Union
from bson.objectid import ObjectId
from .. import dependencies as deps
from pymongo.client_session import ClientSession
from pymongo import MongoClient
from pprint import pprint


app = APIRouter()


@app.get("/find_one")
async def find_one(doc_id: Union[str, None] = None,
                   client: MongoClient = Depends(deps.get_client()),
                   session: ClientSession = Depends(deps.get_db())):
    collection = client.get_database("test-db").get_collection("event")
    bson_id = ObjectId(doc_id)
    find_json = collection.find_one({"_id": bson_id}, session=session)
    pprint(find_json)

    return find_json
