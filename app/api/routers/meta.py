from pprint import pprint
from typing import Any

from fastapi import APIRouter, HTTPException, Depends

from models.meta import Meta, UpdateMeta
from .. import dependencies as deps

router = APIRouter()


# 1. create
@router.post("/create/{data_type}", response_description="")
async def create_meta(
        data_type: str,
        meta: Meta,
        file_list: Any = Depends(deps.file_list)
) -> dict:
    meta.data_type = data_type
    meta.list_in_dir = file_list
    meta.count_in_dir = len(file_list)

    await meta.create()
    result = await meta.get(meta.id)

    return {
        "result": result,
        "message": "meta {} create success".format(data_type)
    }


# 2. read
@router.get("/read_one/{data_type}", response_description="")
async def read_one_meta(
        data_type: str
) -> dict:
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


# 3. update
@router.put("/update_one/{data_type}")
async def update_one_meta(
        data_type: str,
        req: UpdateMeta
) -> dict:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    meta = await Meta.find_one(Meta.data_type == data_type)
    if not meta:
        raise HTTPException(
            status_code=404,
            detail="Meta (data_type: {}) not found!".format(data_type)
        )
    meta.data_type = data_type
    await meta.update(update_query)

    return {
        "result": meta,
        "message": "update_one_meta success"
    }


# 4. delete -> unuse
@router.delete("/delete/{data_type}")
async def delete_meta_one(
        data_type: str,
) -> dict:

    await Meta.find(Meta.data_type == data_type).delete()

    return {
        "message": "delete meta {} collection".format(data_type)
    }