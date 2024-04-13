from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from backend import schemas, services, settings

router = APIRouter()


def get_shodan():
    if settings.SHODAN_API_KEY is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Shodan is not configured correctly",
        )

    return services.Shodan(settings.SHODAN_API_KEY)


def get_censys():
    if settings.CENSYS_APP_ID is None or settings.CENSYS_SECRET is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Censys is not configured correctly",
        )

    return services.Censys(settings.CENSYS_APP_ID, settings.CENSYS_SECRET)


Shodan = Annotated[services.Shodan, Depends(get_shodan)]
Censys = Annotated[services.Censys, Depends(get_censys)]


@router.get("/shodan")
async def shodan(query: str, *, shodan: Shodan) -> schemas.Count:
    return schemas.Count(count=await shodan.call(query))


@router.get("/censys")
async def censys(query: str, *, censys: Censys):
    return schemas.Count(count=await censys.call(query))
