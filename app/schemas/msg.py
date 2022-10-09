from typing import Any

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
    result: Any
