from typing import Union
from pprint import pprint

from fastapi import APIRouter, Depends
from pymongo import MongoClient
from bson.objectid import ObjectId

from .. import dependencies as deps

router = APIRouter()


@router.get("/")
def test_one():
    return 1


@router.get("/find_one")
def find_one(doc_id: Union[str, None] = None,
             client: MongoClient = Depends(deps.get_client),
             # session: ClientSession = Depends(deps.get_session)
             ):
    collection = client.get_database("test-db").get_collection("event")
    session = client.start_session()
    bson_id = ObjectId(doc_id)
    find_json = collection.find_one({"_id": bson_id}, session=session)
    pprint(find_json)

    return find_json['event']
