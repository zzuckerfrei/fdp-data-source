from pprint import pprint

from fastapi import APIRouter, HTTPException

from models.meta import Meta, UpdateMeta

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


# 3. update
@router.put("/update_one/{data_type}")
async def update_one_meta(data_type, req: UpdateMeta) -> dict:
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
