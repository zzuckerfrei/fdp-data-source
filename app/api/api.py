from fastapi import APIRouter

# from .routers import test_router
# from .routers import competition
from .routers import meta

api_router = APIRouter()
# api_router.include_router(test_router.router)
# api_router.include_router(competition.router, prefix="/competition")
api_router.include_router(meta.router, prefix="/meta")
