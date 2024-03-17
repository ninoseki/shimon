from urllib.parse import urljoin, urlparse, urlunparse

import httpx
from returns.functions import raise_exception
from returns.future import FutureResultE, future_safe
from returns.pipeline import flow, is_successful
from returns.pointfree import bind
from returns.unsafe import unsafe_perform_io

from backend import schemas
from backend.utils import (
    get_content_type,
    get_md5,
    get_mmh3,
    get_sha1,
    get_sha256,
    get_soup,
)

from .abstract import AbstractService

LINK_RELS = [
    "icon",
    "shortcut icon",
    "apple-touch-icon",
    "apple-touch-icon-precomposed",
]


def is_absolute(url: str):
    return bool(urlparse(url).netloc)


def get_default_favicon_url(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, "favicon.ico", "", "", ""))


def get_favicon_urls_from_html(url: str, html: str) -> list[str]:
    soup = get_soup(html)

    link_tags = set()
    for rel in LINK_RELS:
        for link_tag in soup.find_all(
            "link",
            attrs={"rel": lambda r: r and r.lower() == rel, "href": True},  # noqa: B023
        ):
            link_tags.add(link_tag)

    icons: list[str] = []
    for tag in link_tags:
        href = tag.get("href", "") or tag.get("content", "")
        href = href.strip()

        if not href or href.startswith("data:image/"):
            continue

        url_parsed = href if is_absolute(href) else urljoin(url, href)

        # repair '//cdn.network.com/favicon.png' or `icon.png?v2`
        scheme = urlparse(url).scheme
        url_parsed = urlparse(url_parsed, scheme=scheme)

        url = url_parsed.geturl()
        if url not in icons:
            icons.append(url)

    return icons


@future_safe
async def get_url(
    url: str,
    *,
    params: dict | None = None,
    raise_for_status: bool = True,
    follow_redirects: bool = True,
) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        res = await client.get(url, params=params, follow_redirects=follow_redirects)
        if raise_for_status:
            res.raise_for_status()

    return res


@future_safe
async def get_favicon(url: str) -> schemas.Favicon:
    @future_safe
    async def convert(res: httpx.Response):
        return schemas.Favicon(
            content_type=get_content_type(res),
            md5=get_md5(res),
            mmh3=get_mmh3(res),
            sha1=get_sha1(res),
            sha256=get_sha256(res),
            url=str(res.url),
        )

    f_result: FutureResultE[schemas.Favicon] = flow(get_url(url), bind(convert))
    result = await f_result.awaitable()
    return unsafe_perform_io(result.alt(raise_exception).unwrap())


class Favicon(AbstractService):
    async def call(self, response: httpx.Response) -> schemas.Favicon | None:
        favicon_urls = get_favicon_urls_from_html(str(response.url), response.text)
        favicon_urls.append(get_default_favicon_url(str(response.url)))

        for url in favicon_urls:
            favicon_result = await get_favicon(url)
            if is_successful(favicon_result):
                return unsafe_perform_io(favicon_result.unwrap())

        return None
