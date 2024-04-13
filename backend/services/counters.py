import httpx
from starlette.datastructures import Secret


class Shodan:
    def __init__(self, api_key: Secret):
        self.api_key = api_key

    async def call(self, query: str):
        async with httpx.AsyncClient(base_url="https://api.shodan.io") as client:
            res = await client.get(
                "/shodan/host/search", params={"key": str(self.api_key), "query": query}
            )
            res.raise_for_status()

        return res.json()["total"]


class Censys:
    def __init__(
        self,
        app_id: Secret,
        secret: Secret,
    ):
        self.app_id = app_id
        self.secret = secret

    async def call(self, query: str):
        auth = httpx.BasicAuth(username=str(self.app_id), password=str(self.secret))

        async with httpx.AsyncClient(
            base_url="https://search.censys.io", auth=auth
        ) as client:
            res = await client.get("/api/v2/hosts/search", params={"q": query})
            res.raise_for_status()

        return res.json()["result"]["total"]
