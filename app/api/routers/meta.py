from pprint import pprint

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from models.meta import Meta

router = APIRouter()


# 1. create
@router.post("/create/{data_type}", response_description="")
async def create_meta(data_type, meta: Meta) -> dict:
    meta.data_type = data_type
    await meta.create()
    result = await meta.get(meta.id)

    return {
        "result": result,
        "message": "meta {} create success".format(data_type)
    }


# 2. read
@router.get("/read_one/{data_type}", response_description="")
async def read_one_meta(data_type) -> dict:
    result = await Meta.find_one(Meta.data_type == data_type)

    return {
        "result": result,
        "message": "read_one_meta {} success".format(data_type)
    }


@router.get("/read_all/", response_description="")
async def read_all_meta() -> dict:
    result = await Meta.find_all().to_list()

    return {
        "result": result,
        "message": "read_all_meta success"
    }


# 3. udpate
@router.put("/update_one/{data_type}")
async def update_one_meta(data_type, meta: Meta) -> dict:
    await meta.update()

    return {
        "result": result,
        "message": "update_one_meta success"
    }

# 4. delete -> unuse
