from fastapi import APIRouter

from backend.api.endpoints import counters, fingerprint

api_router = APIRouter()
api_router.include_router(
    fingerprint.router, prefix="/fingerprint", tags=["fingerprint"]
)
api_router.include_router(counters.router, prefix="/counters", tags=["counters"])
