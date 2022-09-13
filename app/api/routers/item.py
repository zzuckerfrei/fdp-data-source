import json
from pprint import pprint

from fastapi import APIRouter, Depends, HTTPException
from typing import Any

from .. import dependencies as deps
from models.item import Item
from models.meta import Meta

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
async def create_item(data_type, org_name, file_list: Any = Depends(deps.finder),
                      data_model: Any = Depends(deps.checker)) -> dict:
    """
    :param data_model:
    :param data_type: 데이터 타입 competition, match, lineup, event
    :param org_name: 마지막으로 적재된 파일 이름(경로)
    :param file_list:
    :return:
    """
    try:
        # 임시) data_type, org_name 기반으로 dir, json 찾아서 read
        # 타입별 메타 정보 조회, 그 다음 파일 읽어서 model에 담기
        meta = await Meta.find_one(Meta.data_type == data_type)

        target_file = meta.list_in_dir[meta.list_in_dir.index(org_name) + 1]
        print("target file is {}".format(target_file))

        with open(target_file, 'r') as f:
            data = json.load(f)
            print(data[0])
        print(len(data))
        # to be) 에어플로우로부터 meta db에서 다음 파일 경로 리턴받기
        # 리턴받은 경로의 파일만 조회하여 아래 model에 담기

        # model 담기
        result = []
        for one in data:
            model = data_model(data_type=data_type,
                               org_name=target_file,
                               data=one,
                               to_dw=False)

            # insert 실행
            await model.create()
            result.extend(await model.get(model.id))
            # pprint(result)

        # Meta 정보 update

        return {
            "result": result,
            "meta": data[0],
            # "message": "item {} create success".format(temp_result)
        }

    except Exception as e:
        raise HTTPException(  # httpexception써도 됨??
            status_code=404,
            detail="error = {}".format(e)
        )


# 4. delete
@router.delete("/delete")
async def delete_item_all(data_type, data_model: Any = Depends(deps.checker)):

    await data_model.find(data_model.data_type == data_type).delete()

    return {
        "ressult": "delete all {} collection".format(data_type)
    }


####################################################################################  나중에 개발


# 2. read - find by : data_type, org_name
@router.get("/read_one", response_description="")
async def read_one_item(data_type, org_name, data_model: Any = Depends(deps.checker)) -> dict:
    return {
        # "result": result,
        "message": "read_one_meta {} success".format(data_type)
    }

# 3. update -> unuse