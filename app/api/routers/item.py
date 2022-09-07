from pprint import pprint

from fastapi import APIRouter, Depends, Header, HTTPException, Body
from typing import Any

from models.meta import Meta, UpdateMeta
from config import settings
from .. import dependencies as deps

router = APIRouter()


##
class DataTypeChecker:
    def __init__(self, data_type: str):
        self.data_class = settings.DATA_TYPE[data_type][0]


# 1. create
@router.post("/create", response_description="")
async def create_item(data_type: str, req: dict) -> dict:

    req = {k: v for k, v in req.items() if v is not None}



    return {
        # "result": result,
        "message": "meta {} create success".format(data_type)
    }
