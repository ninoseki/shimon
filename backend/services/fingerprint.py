import contextlib
from dataclasses import dataclass, field

import httpx
from returns.functions import raise_exception
from returns.future import FutureResultE, future_safe
from returns.pipeline import flow
from returns.pointfree import bind
from returns.unsafe import unsafe_perform_io

from backend import schemas

from .abstract import AbstractService
from .certificate import Certificate
from .dns import DNS
from .favicon import Favicon
from .html import HTML
from .tls import TLS
from .tracker import Tracker
from .whois import Whois


@dataclass
class Container:
    response: httpx.Response

    html: schemas.HTML | None = field(default=None)
    dns: schemas.DNS | None = field(default=None)
    tracker: schemas.Tracker | None = field(default=None)
    whois: schemas.Whois | None = field(default=None)
    favicon: schemas.Favicon | None = field(default=None)
    certificate: schemas.Certificate | None = field(default=None)
    tls: schemas.TLS | None = field(default=None)


@future_safe
async def get_url(url: str) -> Container:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url, follow_redirects=True)
        return Container(response=response)


@future_safe
async def get_whois(container: Container) -> Container:
    container.whois = await Whois().call(container.response)
    return container


@future_safe
async def get_certificate(container: Container) -> Container:
    with contextlib.suppress(Exception):
        container.certificate = await Certificate().call(container.response)

    return container


@future_safe
async def get_favicon(container: Container) -> Container:
    with contextlib.suppress(Exception):
        container.favicon = await Favicon().call(container.response)

    return container


@future_safe
async def get_html(container: Container) -> Container:
    with contextlib.suppress(Exception):
        container.html = await HTML().call(container.response)

    return container


@future_safe
async def get_tracker(container: Container) -> Container:
    try:
        container.tracker = await Tracker().call(container.response)
    except Exception:
        container.tracker = schemas.Tracker()

    return container


@future_safe
async def get_dns(container: Container) -> Container:
    try:
        container.dns = await DNS().call(container.response)
    except Exception:
        container.dns = schemas.DNS()

    return container


@future_safe
async def get_tls(container: Container) -> Container:
    with contextlib.suppress(Exception):
        container.tls = await TLS().call(container.response)

    return container


class Fingerprint(AbstractService):
    async def call(self, url: str) -> schemas.Fingerprint:
        f_result: FutureResultE[Container] = flow(
            url,
            get_url,
            bind(get_certificate),
            bind(get_dns),
            bind(get_favicon),
            bind(get_html),
            bind(get_tls),
            bind(get_tracker),
            bind(get_whois),
        )
        result = (await f_result.awaitable()).alt(raise_exception).unwrap()
        container = unsafe_perform_io(result)
        return schemas.Fingerprint(
            html=container.html,  # type: ignore
            dns=container.dns,  # type: ignore
            tracker=container.tracker,  # type: ignore
            whois=container.whois,  # type: ignore
            favicon=container.favicon,
            certificate=container.certificate,
            tls=container.tls,
            headers=dict(container.response.headers),
        )
