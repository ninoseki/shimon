from fastapi import APIRouter

from app.api.endpoints import fingerprint

api_router = APIRouter()
api_router.include_router(
    fingerprint.router, prefix="/fingerprint", tags=["fingerprint"]
)
