from .api_model import APIModel


class Certificate(APIModel):
    sha1: str
    sha256: str
    serial: str
