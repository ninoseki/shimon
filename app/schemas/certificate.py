import ssl
from typing import Optional
from urllib.parse import urlparse

import requests
from fastapi_utils.api_model import APIModel
from OpenSSL import crypto


class Certificate(APIModel):
    sha1: str
    sha256: str
    serial: str

    @classmethod
    def build_from_response(
        cls, response: requests.Response
    ) -> Optional["Certificate"]:
        if not response.url.startswith("https://"):
            return None

        parsed = urlparse(response.url)

        cert_pem = ssl.get_server_certificate((parsed.netloc, 443))
        cert: crypto.X509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)

        sha256 = cert.digest("sha256").decode().replace(":", "").lower()
        sha1 = cert.digest("sha1").decode().replace(":", "").lower()
        serial_number = str(cert.get_serial_number())

        return cls(
            sha1=sha1,
            sha256=sha256,
            serial=serial_number,
        )
