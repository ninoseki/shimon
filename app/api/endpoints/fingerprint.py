from urllib.parse import urlparse

import requests
from fastapi import APIRouter, HTTPException

from app.schemas.fingerprint import Fingerprint
from app.schemas.utils import get_response

router = APIRouter()


def validate_url(url: str) -> bool:
    parsed = urlparse(url)

    valid_schemes = ["http", "https"]
    if parsed.scheme not in valid_schemes:
        return False

    valid_paths = [
        "",
        "/",
    ]
    if parsed.path not in valid_paths:
        return False

    return True


@router.get(
    "/calculate",
    response_model=Fingerprint,
    response_description="Fingerprint of a website",
    summary="Get a fingerprint of an HTML or favicon",
    description="Returns a fingerprint of a website",
)
async def calculate(url: str):
    if not validate_url(url):
        raise HTTPException(status_code=400, detail=f"{url} is not a valid URL")

    try:
        response = get_response(url)
    except (requests.HTTPError, requests.ConnectionError) as e:
        raise HTTPException(status_code=500, detail=f"Cannot get {url}: {e}")

    try:
        return await Fingerprint.build_from_response(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
