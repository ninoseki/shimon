from urllib.parse import urlparse


def url_domain(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc


def decode_str_byte(v: str | bytes, *, encoding: str = "utf=8") -> str:
    if isinstance(v, bytes):
        return v.decode(encoding)

    return v
