import base64
import hashlib

import httpx
import mmh3
from bs4 import BeautifulSoup


def get_soup(html: str):
    return BeautifulSoup(html, features="html.parser")


def get_content_type(response: httpx.Response) -> str:
    return response.headers.get("Content-Type", "")


def get_mmh3(response: httpx.Response) -> int:
    content_type = get_content_type(response)
    if "text/html" in content_type:
        return mmh3.hash(response.text)

    b64 = base64.encodebytes(response.content)
    return mmh3.hash(b64)


def get_md5(response: httpx.Response) -> str:
    return hashlib.md5(response.content).hexdigest()


def get_sha256(response: httpx.Response) -> str:
    return hashlib.sha256(response.content).hexdigest()


def get_sha1(response: httpx.Response) -> str:
    return hashlib.sha1(response.content).hexdigest()


def decode_str_byte(v: str | bytes, *, encoding: str = "utf=8") -> str:
    if isinstance(v, bytes):
        return v.decode(encoding)

    return str(v)
