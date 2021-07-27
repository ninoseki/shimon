from typing import Optional

import requests
from fastapi_utils.api_model import APIModel

from app.schemas.certificate import Certificate
from app.schemas.dns import DNS
from app.schemas.favicon import Favicon
from app.schemas.html import HTML
from app.schemas.tracker import Tracker
from app.schemas.whois import Whois


class Fingerprint(APIModel):
    html: HTML
    dns: DNS
    tracker: Tracker
    whois: Whois

    favicon: Optional[Favicon]
    certificate: Optional[Certificate]

    @classmethod
    async def build_from_response(cls, response: requests.Response):
        html = HTML.build_from_response(response)
        dns = await DNS.build_from_response(response)
        tracker = Tracker.build_from_response(response)
        whois = await Whois.build_from_response(response)

        favicon = Favicon.build_from_response(response)
        certificate = Certificate.build_from_response(response)

        return cls(
            html=html,
            certificate=certificate,
            favicon=favicon,
            dns=dns,
            tracker=tracker,
            whois=whois,
        )
