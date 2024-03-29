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


class HTML(AbstractService):
    async def call(self, response: httpx.Response) -> schemas.HTML:
        title: str | None = None

        soup = get_soup(response.text)
        title_elem = soup.find("title")
        if title_elem is not None:
            title = title_elem.text

        return schemas.HTML(
            content_type=get_content_type(response),
            md5=get_md5(response),
            mmh3=get_mmh3(response),
            sha1=get_sha1(response),
            sha256=get_sha256(response),
            url=str(response.url),
            title=title,
        )
