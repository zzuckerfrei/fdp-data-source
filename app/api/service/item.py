import json
from datetime import datetime

from typing import Any

from fastapi import HTTPException

from models.meta import Meta


# 1 create
async def create_item_service(data_type: str,
                              org_name: str,
                              item_model: Any):
    try:
        with open(org_name, 'r') as f:
            data = json.load(f)

        # model 담기
        result = 0
        for one in data:
            model = item_model(data_type=data_type,
                               org_name=org_name,
                               data=one,
                               to_dw=False)

            # insert 실행
            await model.create()
            result += 1

        return result

    except Exception as e:
        raise HTTPException(  # httpexception써도 됨??
            status_code=404,
            detail="error = {}".format(e)
        )


# 2 read
async def select_item_one(org_name: str,
                          item_model: Any):
    try:
        item = await item_model.find_one(item_model.org_name == org_name)

        return item

    except Exception as e:
        print(e)
        raise Exception


# 4 delete
async def delete_item_all_service(data_type: str,
                                  item_model: Any):
    try:
        # delete item
        await item_model.find(item_model.data_type == data_type).delete()

        # update meta
        meta = await Meta.find_one(Meta.data_type == data_type)
        meta.list_in_db = list()
        meta.count_in_db = len(meta.list_in_db)
        meta.last_update = datetime.now()

        update_query = {"$set": {
            field: value for field, value in dict(meta).items()
        }}

        await meta.update(update_query)

    except Exception as e:
        raise HTTPException(  # httpexception써도 됨??
            status_code=404,
            detail="error = {}".format(e)
        )



