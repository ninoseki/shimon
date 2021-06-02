import requests

from app.schemas.resource import Resource
from app.schemas.utils import get_content_type, get_md5, get_mmh3, get_sha1, get_sha256


class HTML(Resource):
    @classmethod
    def build_from_response(cls, response: requests.Response) -> "HTML":
        return cls(
            content_type=get_content_type(response),
            md5=get_md5(response),
            mmh3=get_mmh3(response),
            sha1=get_sha1(response),
            sha256=get_sha256(response),
            url=response.url,
        )
