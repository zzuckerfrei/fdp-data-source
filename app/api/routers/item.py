from pprint import pprint

from fastapi import APIRouter, Depends
from typing import Any

from .. import dependencies as deps
from models.item import Item

router = APIRouter()


# 1. create
@router.post("/create", response_description="")
async def create_item(item: Item, data_model: Any = Depends(deps.checker)) -> dict:
    model = data_model(data_type=item.data_type,
                       org_name=item.org_name,
                       data=item.data,
                       to_dw=item.to_dw)
    await model.create()
    result = await model.get(model.id)
    pprint(result)

    return {
        "result": result,
        "message": "item {} create success".format(data_model)
    }


# 2. read
@router.get("/read_one", response_description="")
async def read_one_item(data_type) -> dict:
    result = await Meta.find_one(Meta.data_type == data_type)

    return {
        "result": result,
        "message": "read_one_meta {} success".format(data_type)
    }
