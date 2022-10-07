from fastapi import FastAPI

from api.api import api_router
from config import settings
from database import init_db

app = FastAPI(title="fdp-data-source api server", openapi_url=f"{settings.API_V1_STR}/openapi.json")


## todo 적용되는것인가?
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

##


@app.on_event("startup")
async def start_db():
    await init_db()
# on_event(shutdown) 추가??

app.include_router(api_router, prefix=settings.API_V1_STR)

# uvicorn main:app --host 127.0.0.1 --port 8000 --timeout-keep-alive 500 --reload

