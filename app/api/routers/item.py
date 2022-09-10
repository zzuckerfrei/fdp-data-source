from pprint import pprint

from fastapi import APIRouter, Depends
from typing import Any

from .. import dependencies as deps
from models.item import Item

router = APIRouter()


# 1.1 create - crud api
@router.post("/create_temp", response_description="")
async def create_item_temp(item: Item, data_model: Any = Depends(deps.checker)) -> dict:
    model = data_model(data_type=item.data_type,
                       org_name=item.org_name,
                       data=item.data,
                       to_dw=item.to_dw)
    await model.create()
    result = await model.get(model.id)
    pprint(result)

    # Meta update필요
    return {
        "result": result,
        "message": "item {} create success".format(data_model)
    }


# 1.2 create - 실제 airflow가 호출할 api
@router.post("/create", response_description="")
async def create_item(data_type, org_name, data_model: Any = Depends(deps.checker)) -> dict:
    # data_type, org_name 기반으로 dir, json 찾아서 read

    # model 담기
    model = data_model(data_type=item.data_type,
                       org_name=item.org_name,
                       data=item.data,
                       to_dw=item.to_dw)

    # insert 실행
    await model.create()
    result = await model.get(model.id)
    pprint(result)

    # Meta update필요
    return {
        "result": result,
        "message": "item {} create success".format(data_model)
    }


####################################################################################  나중에 개발

# 2. read - find by : data_type, org_name
@router.get("/read_one", response_description="")
async def read_one_item(data_type, org_name, data_model: Any = Depends(deps.checker)) -> dict:
    return {
        # "result": result,
        "message": "read_one_meta {} success".format(data_type)
    }
