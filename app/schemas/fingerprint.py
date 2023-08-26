import requests
from pydantic import Field

from .api_model import APIModel
from .certificate import Certificate
from .dns import DNS
from .favicon import Favicon
from .html import HTML
from .tracker import Tracker
from .whois import Whois


class Fingerprint(APIModel):
    html: HTML
    dns: DNS
    tracker: Tracker
    whois: Whois

    favicon: Favicon | None
    certificate: Certificate | None

    headers: dict[str, str] = Field(default_factory=dict)

    @classmethod
    async def parse_response(cls, response: requests.Response):
        dns = await DNS.parse_response(response)
        whois = await Whois.parse_response(response)

        html = HTML.parse_response(response)
        tracker = Tracker.parse_response(response)
        favicon = Favicon.parse_response(response)
        certificate = Certificate.parse_response(response)

        return cls(
            html=html,
            certificate=certificate,
            favicon=favicon,
            dns=dns,
            tracker=tracker,
            whois=whois,
            headers=dict(response.headers),
        )
