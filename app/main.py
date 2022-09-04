from fastapi import FastAPI

from api.api import api_router
from config import settings
from database import init_db

app = FastAPI(title="title test", openapi_url=f"{settings.API_V1_STR}/openapi.json")


@app.on_event("startup")
async def start_db():
    await init_db()
# on_event(shutdown) 추가??

app.include_router(api_router, prefix=settings.API_V1_STR)



