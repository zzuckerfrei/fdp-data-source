from fastapi import APIRouter
from .routers import test_router


api_router = APIRouter()
api_router.include_router(test_router)