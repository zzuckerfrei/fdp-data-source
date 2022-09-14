from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional, List


# 임시 meta 보관소
class Meta(Document):
    data_type: str = None
    count_in_dir: int
    list_in_dir: List[str]
    count_in_db: int
    list_in_db: List[str]
    last_update: datetime = datetime.now()

    class Settings:
        name = "meta"

    class Config:
        schema_extra = {
            "example": {
                "data_type": "match",
                "count_in_dir": 5,
                "list_in_dir": ["1.json", "2.json", "3.json", "4.json", "5.json"],
                "count_in_db": 0,
                "list_in_db": [],
                "last_update": datetime.now()
            }
        }


class UpdateMeta(BaseModel):
    data_type: Optional[str]
    count_in_dir: Optional[int]
    list_in_dir: Optional[List[str]]
    count_in_db: Optional[int]
    list_in_db: Optional[List[str]]
    last_update: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "data_type": "match",
                "count_in_dir": 5,
                "list_in_dir": ["1.json", "2.json", "3.json", "4.json", "5.json"],
                "count_in_db": 4,
                "list_in_db": ["1.json", "2.json", "3.json", "4.json"],
                "last_update": datetime.now()
            }
        }
