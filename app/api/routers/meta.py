from typing import Any

from fastapi import APIRouter, HTTPException, Depends

from models.meta import Meta, UpdateMeta
from .. import dependencies as deps
import schemas

router = APIRouter()


# 1. create
@router.get("/create/{data_type}", response_model=schemas.Msg, response_description="")
async def create_meta(
        data_type: str,
        file_list: Any = Depends(deps.file_list)
) -> Any:
    """
    최초 meta 데이터 저장시 호출 \n
    meta를 postgres에 저장하게 되면서 await meta.create()는 사용하지 않게 됨 20221031\n

    :param data_type: 데이터 타입 competition, match, lineup, event \n
    :param file_list: 데이터 타입별 json 파일 목록 \n
    :return: {"data_type" : str, "list_in_dir" : list, "count_dir_dir" : int}
    """

    return {
        "msg": "meta {} create success".format(data_type),
        "result": {"data_type": data_type,
                   "list_in_dir": file_list,
                   "count_in_dir": len(file_list)}
    }


# 2. read
@router.get("/read_one/{data_type}", response_model=schemas.Msg, response_description="")
async def read_one_meta(
        data_type: str
) -> Any:
    result = await Meta.find_one(Meta.data_type == data_type)

    return {
        "result": result,
        "msg": "read_one_meta {} success".format(data_type)
    }


@router.get("/read_all/", response_model=schemas.Msg, response_description="")
async def read_all_meta(
) -> Any:
    result = await Meta.find_all().to_list()

    return {
        "result": result,
        "msg": "read_all_meta success"
    }


# 3. update
@router.put("/update_one/{data_type}", response_model=schemas.Msg)
async def update_one_meta(
        data_type: str,
        req: UpdateMeta
) -> Any:
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
        "msg": "update_one_meta success"
    }


# 4. delete -> unuse
@router.delete("/delete/{data_type}", response_model=schemas.Msg)
async def delete_meta_one(
        data_type: str,
) -> Any:
    await Meta.find(Meta.data_type == data_type).delete()

    return {
        "msg": "delete meta {} collection".format(data_type)
    }
