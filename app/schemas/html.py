import requests
from pydantic import Field

from app.schemas.resource import Resource
from app.schemas.utils import get_content_type, get_md5, get_mmh3, get_sha1, get_sha256

from .utils import get_soup


class HTML(Resource):
    title: str | None = Field(default=None)

    @classmethod
    def build_from_response(cls, response: requests.Response) -> "HTML":
        title: str | None = None

        soup = get_soup(response.text)
        title_elem = soup.find("title")
        if title_elem is not None:
            title = title_elem.text

        return cls(
            content_type=get_content_type(response),
            md5=get_md5(response),
            mmh3=get_mmh3(response),
            sha1=get_sha1(response),
            sha256=get_sha256(response),
            url=response.url,
            title=title,
        )
