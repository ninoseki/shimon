import socket
import ssl
from typing import Optional, cast

import requests
from OpenSSL import crypto

from app.utils import url_domain

from .api_model import APIModel


class Certificate(APIModel):
    sha1: str
    sha256: str
    serial: str

    @classmethod
    def parse_response(cls, response: requests.Response) -> Optional["Certificate"]:
        if not response.url.startswith("https://"):
            return None

        hostname = url_domain(response.url)
        port = 443

        context = ssl.create_default_context()
        connection = socket.create_connection((hostname, port))
        ssl_socket = context.wrap_socket(connection, server_hostname=hostname)
        peer_cert = cast(bytes, ssl_socket.getpeercert(True))
        pem_cert = ssl.DER_cert_to_PEM_cert(peer_cert)
        cert: crypto.X509 = crypto.load_certificate(crypto.FILETYPE_PEM, pem_cert)

        sha256 = cert.digest("sha256").decode().replace(":", "").lower()
        sha1 = cert.digest("sha1").decode().replace(":", "").lower()
        serial_number = str(cert.get_serial_number())

        return cls(
            sha1=sha1,
            sha256=sha256,
            serial=serial_number,
        )
