import json
from datetime import datetime

from typing import Any

from fastapi import HTTPException

from models.meta import Meta


async def create_item_service(data_type: str,
                              org_name: str,
                              item_model: Any):
    try:
        # 임시) data_type, org_name 기반으로 dir, json 찾아서 read
        # 타입별 메타 정보 조회, 그 다음 파일 읽어서 model에 담기
        meta = await Meta.find_one(Meta.data_type == data_type)

        # target_file = meta.list_in_dir[meta.list_in_dir.index(org_name) + 1]  # index+1 로직 수정 20220915
        target_file = meta.list_in_dir[meta.list_in_dir.index(org_name)]
        print("target file is {}".format(target_file))

        with open(target_file, 'r') as f:
            data = json.load(f)

            # to be) 에어플로우로부터 meta db에서 다음 파일 경로 리턴받기
            # 리턴받은 경로의 파일만 조회하여 아래 model에 담기

            # model 담기
        result = 0
        for one in data:
            model = item_model(data_type=data_type,
                               org_name=target_file,
                               data=one,
                               to_dw=False)

            # insert 실행
            await model.create()
            result += 1

        # Meta 정보 update
        # 일단은 여기서 업데이트 로직을 실행하지만, 추후 airflow postgres오퍼레이터 사용해서 업데이트하기
        meta.list_in_db.append(target_file)
        meta.list_in_db = list(set(meta.list_in_db))
        meta.count_in_db = len(meta.list_in_db)
        meta.last_update = datetime.now()

        update_query = {"$set": {
            field: value for field, value in dict(meta).items()
        }}

        await meta.update(update_query)

        return result

    except Exception as e:
        raise HTTPException(  # httpexception써도 됨??
            status_code=404,
            detail="error = {}".format(e)
        )


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
