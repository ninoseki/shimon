import base64
import hashlib
from functools import lru_cache

import mmh3
import requests
from bs4 import BeautifulSoup


@lru_cache(maxsize=128)
def get_soup(html: str):
    return BeautifulSoup(html, features="html.parser")


def get_response(url: str) -> requests.Response:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    return response


def get_content_type(response: requests.Response) -> str:
    return response.headers.get("Content-Type", "")


def get_mmh3(response: requests.Response) -> int:
    content_type = get_content_type(response)
    if "text/html" in content_type:
        return mmh3.hash(response.text)

    b64 = base64.encodebytes(response.content)
    return mmh3.hash(b64)


def get_md5(response: requests.Response) -> str:
    return hashlib.md5(response.content).hexdigest()


def get_sha256(response: requests.Response) -> str:
    return hashlib.sha256(response.content).hexdigest()


def get_sha1(response: requests.Response) -> str:
    return hashlib.sha1(response.content).hexdigest()
