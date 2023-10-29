import httpx

from backend import jarm, schemas

from .abstract import AbstractService


class TLS(AbstractService):
    async def call(self, response: httpx.Response) -> schemas.TLS | None:
        if response.url.scheme == "http":
            return None

        results = await jarm.scan(response.url.host)
        return schemas.TLS(jarm=results[-1])
