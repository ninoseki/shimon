from typing import Optional

import requests
from fastapi_utils.api_model import APIModel
from ioc_finder import parse_google_adsense_ids, parse_google_analytics_ids


class Tracker(APIModel):
    google_adsense_id: Optional[str]
    google_analytics_id: Optional[str]

    @classmethod
    def build_from_response(cls, response: requests.Response) -> "Tracker":
        html = response.text

        adsense_id: Optional[str] = None
        adsense_ids = parse_google_adsense_ids(html)
        if len(adsense_ids) == 1:
            adsense_id = adsense_ids[0]

        analytics_id: Optional[str] = None
        analytics_ids = parse_google_analytics_ids(html)
        if len(analytics_ids) == 1:
            analytics_id = analytics_ids[0]

        return cls(google_adsense_id=adsense_id, google_analytics_id=analytics_id)
