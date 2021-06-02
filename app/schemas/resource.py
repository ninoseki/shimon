from fastapi_utils.api_model import APIModel


class Resource(APIModel):
    content_type: str
    md5: str
    mmh3: int
    sha1: str
    sha256: str
    url: str
