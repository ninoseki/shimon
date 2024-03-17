from dataclasses import dataclass

import aiometer
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


@future_safe
async def get_url(url: str) -> httpx.Response:
    async with httpx.AsyncClient(verify=False) as client:
        return await client.get(url, follow_redirects=True)


@future_safe
async def get_whois(res: httpx.Response) -> schemas.Whois:
    return await Whois().call(res)


@future_safe
async def get_certificate(res: httpx.Response) -> schemas.Certificate | None:
    return await Certificate().call(res)


@future_safe
async def get_favicon(res: httpx.Response) -> schemas.Favicon | None:
    return await Favicon().call(res)


@future_safe
async def get_html(res: httpx.Response) -> schemas.HTML:
    return await HTML().call(res)


@future_safe
async def get_tracker(res: httpx.Response) -> schemas.Tracker:
    return await Tracker().call(res)


@future_safe
async def get_dns(res: httpx.Response) -> schemas.DNS:
    return await DNS().call(res)


@future_safe
async def get_tls(res: httpx.Response) -> schemas.TLS | None:
    return await TLS().call(res)


@future_safe
async def get_fingerprint(res: httpx.Response) -> schemas.Fingerprint:
    (
        certificate_result,
        dns_result,
        favicon_result,
        html_result,
        tls_result,
        tracker_result,
        whois_result,
    ) = await aiometer.run_all(
        [
            get_certificate(res).awaitable,
            get_dns(res).awaitable,
            get_favicon(res).awaitable,
            get_html(res).awaitable,
            get_tls(res).awaitable,
            get_tracker(res).awaitable,
            get_whois(res).awaitable,
        ]
    )
    certificate: schemas.Certificate | None = unsafe_perform_io(
        certificate_result.value_or(None)  # type: ignore
    )  # type: ignore
    dns: schemas.DNS = unsafe_perform_io(dns_result.value_or(schemas.DNS()))  # type: ignore
    favicon: schemas.Favicon | None = unsafe_perform_io(favicon_result.value_or(None))  # type: ignore
    html: schemas.HTML = unsafe_perform_io(html_result.alt(raise_exception).unwrap())  # type: ignore
    tls: schemas.TLS | None = unsafe_perform_io(tls_result.value_or(None))  # type: ignore
    tracker: schemas.Tracker = unsafe_perform_io(
        tracker_result.value_or(schemas.Tracker())  # type: ignore
    )
    whois: schemas.Whois = unsafe_perform_io(whois_result.value_or(schemas.Whois()))  # type: ignore
    return schemas.Fingerprint(
        certificate=certificate,
        dns=dns,
        favicon=favicon,
        html=html,
        tls=tls,
        tracker=tracker,
        whois=whois,
        headers=dict(res.headers),
    )


class Fingerprint(AbstractService):
    async def call(self, url: str) -> schemas.Fingerprint:
        f_result: FutureResultE[schemas.Fingerprint] = flow(
            url, get_url, bind(get_fingerprint)
        )
        result = (await f_result.awaitable()).alt(raise_exception).unwrap()
        return unsafe_perform_io(result)
