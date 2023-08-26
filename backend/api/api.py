from fastapi import APIRouter

from backend.api.endpoints import fingerprint

api_router = APIRouter()
api_router.include_router(
    fingerprint.router, prefix="/fingerprint", tags=["fingerprint"]
)
