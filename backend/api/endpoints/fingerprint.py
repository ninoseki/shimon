from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, HttpUrl, ValidationError

from backend import schemas, services

router = APIRouter()


class Url(BaseModel):
    url: HttpUrl


@router.get("/calculate")
async def calculate(url: str) -> schemas.Fingerprint:
    try:
        Url(url=url)  # type: ignore
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors()
        ) from e

    try:
        return await services.Fingerprint().call(url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
