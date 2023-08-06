from urllib.parse import urlparse


def url_domain(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc
