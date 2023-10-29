import typing

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

    favicon: Favicon | None = Field(default=None)
    certificate: Certificate | None = Field(default=None)

    headers: dict[str, typing.Any] = Field(default_factory=dict)
