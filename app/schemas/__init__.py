import base64
import hashlib

import mmh3
import requests
from fastapi_utils.api_model import APIModel


def get_content_type(response: requests.Response) -> str:
    return response.headers.get("Content-Type", "")


def get_mmh3(response: requests.Response) -> int:
    content_type = get_content_type(response)
    if "text/html" in content_type:
        return mmh3.hash(response.text)
    else:
        b64 = base64.encodebytes(response.content)
        return mmh3.hash(b64)


def get_md5(response: requests.Response) -> str:
    return hashlib.md5(response.content).hexdigest()


def get_sha256(response: requests.Response) -> str:
    return hashlib.sha256(response.content).hexdigest()


class Hashes(APIModel):
    content_type: str
    md5: str
    mmh3: int
    sha256: str
    url: str

    @classmethod
    def build_from_response(cls, response: requests.Response):
        return cls(
            content_type=get_content_type(response),
            md5=get_md5(response),
            mmh3=get_mmh3(response),
            sha256=get_sha256(response),
            url=response.url,
        )
