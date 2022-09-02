from fastapi import FastAPI

from api.api import api_router
from config import settings


app = FastAPI(title="title test", openapi_url=f"{settings.API_V1_STR}/openapi.json")
app.include_router(api_router, prefix=settings.API_V1_STR)
