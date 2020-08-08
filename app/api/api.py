from fastapi import APIRouter

from app.api.endpoints import hashes

api_router = APIRouter()
api_router.include_router(hashes.router, prefix="/hashes", tags=["hashes"])
