from fastapi import APIRouter, Depends

from .. import dependencies as deps
from ..service.item import *
import schemas

router = APIRouter()


# 1 create - 실제 airflow가 호출할 api
@router.post("/create", response_model=schemas.Msg, response_description="")
async def create_item(
        data_type: str,
        org_name: str,
        item_model: Any = Depends(deps.item_model)
) -> Any:

    result = await create_item_service(data_type, org_name, item_model)

    return {
        "msg": "item {} create success, count : {}".format(data_type, result)
    }


# 2. read - find by : data_type, org_name
@router.get("/read_one", response_model=schemas.Msg, response_description="")
async def read_one_item(
        data_type,
        org_name,
        item_model: Any = Depends(deps.item_model)
) -> dict:

    result = await select_item_one(org_name=org_name, item_model=item_model)

    return {
        "result": result,
        "msg": "read_one_meta {} success".format(data_type)
    }


# 4. delete
@router.delete("/delete", response_model=schemas.Msg, response_description="")
async def delete_item_all(
        data_type: str,
        item_model: Any = Depends(deps.item_model)
) -> Any:
    await delete_item_all_service(data_type, item_model)

    return {
        "msg": "delete all {} collection".format(data_type)
    }


####################################################################################  나중에 개발

# 1.1 create - crud api
# @router.post("/create_temp", response_description="")
# async def create_item_temp(item: Item, data_model: Any = Depends(deps.checker)) -> dict:
#     model = data_model(data_type=item.data_type,
#                        org_name=item.org_name,
#                        data=item.data,
#                        to_dw=item.to_dw)
#     await model.create()
#     result = await model.get(model.id)
#
#     # Meta update필요
#     return {
#         "result": result,
#         "message": "item {} create success".format(data_model)
#     }



# 3. update -> unuse
