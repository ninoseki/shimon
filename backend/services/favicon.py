from urllib.parse import urljoin, urlparse, urlunparse

import httpx

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


class Favicon(AbstractService):
    async def call(self, response: httpx.Response) -> schemas.Favicon | None:
        favicon_urls = get_favicon_urls_from_html(str(response.url), response.text)
        favicon_urls.append(get_default_favicon_url(str(response.url)))

        async with httpx.AsyncClient() as client:
            for url in favicon_urls:
                try:
                    res = await client.get(url)
                    res.raise_for_status()
                    return schemas.Favicon(
                        content_type=get_content_type(res),
                        md5=get_md5(res),
                        mmh3=get_mmh3(res),
                        sha1=get_sha1(res),
                        sha256=get_sha256(res),
                        url=str(res.url),
                    )
                except httpx.HTTPError:
                    pass

        return None
