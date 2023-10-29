import socket
import ssl
from typing import cast

import httpx
from OpenSSL import crypto

from backend import schemas

from .abstract import AbstractService


class Certificate(AbstractService):
    async def call(self, response: httpx.Response) -> schemas.Certificate | None:
        if response.url.scheme == "http":
            return None

        port = 443

        context = ssl.create_default_context()
        connection = socket.create_connection((response.url.host, port))
        ssl_socket = context.wrap_socket(connection, server_hostname=response.url.host)
        peer_cert = cast(bytes, ssl_socket.getpeercert(True))
        pem_cert = ssl.DER_cert_to_PEM_cert(peer_cert)
        cert: crypto.X509 = crypto.load_certificate(crypto.FILETYPE_PEM, pem_cert)  # type: ignore

        sha256 = cert.digest("sha256").decode().replace(":", "").lower()
        sha1 = cert.digest("sha1").decode().replace(":", "").lower()
        serial_number = str(cert.get_serial_number())

        return schemas.Certificate(
            sha1=sha1,
            sha256=sha256,
            serial=serial_number,
        )
