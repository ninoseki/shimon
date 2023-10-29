import httpx
from ioc_finder import parse_google_adsense_ids, parse_google_analytics_ids

from backend import schemas

from .abstract import AbstractService


class Tracker(AbstractService):
    async def call(
        self,
        response: httpx.Response,
    ) -> schemas.Tracker:
        html = response.text

        adsense_id: str | None = None
        adsense_ids = parse_google_adsense_ids(html)
        if len(adsense_ids) == 1:
            adsense_id = adsense_ids[0]

        analytics_id: str | None = None
        analytics_ids = parse_google_analytics_ids(html)
        if len(analytics_ids) == 1:
            analytics_id = analytics_ids[0]

        return schemas.Tracker(
            google_adsense_id=adsense_id, google_analytics_id=analytics_id
        )
