from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class Lineup(Document):
    data_type: str
    org_name: str
    data: dict
    to_dw: bool
    last_update: datetime = datetime.now()

    class Settings:
        name = "lineup"

    class Config:
        schema_extra = {
            "example": {
                "data_type": "lineup",
                "org_name": "1.json",
                "data": {
                    "id": "11493e75-0d53-4489-8ccf-a2d2752661ec",
                    "index": 4,
                    "period": 1,
                    "timestamp": "00:00:00.000",
                    "duration": 0.0,
                    "related_events": ["44a69b91-c642-40b1-a615-db11054b3adb"]
                },
                "to_dw": False,
                "last_update": datetime.now()
            }
        }


class UpdateLineup(BaseModel):
    data_type: Optional[str]
    org_name: Optional[str]
    data: Optional[dict]
    to_dw: Optional[bool]
    last_update: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "data_type": "lineup",
                "org_name": "1.json",
                "data": {
                    "id": "11493e75-0d53-4489-8ccf-a2d2752661ec",
                    "index": 4,
                    "period": 1,
                    "timestamp": "00:00:00.000",
                    "duration": 0.0,
                    "related_events": ["44a69b91-c642-40b1-a615-db11054b3adb"]
                },
                "to_dw": True,
                "last_update": datetime.now()
            }
        }
