import asyncwhois
import requests
from pydantic import Field
from whois_parser import WhoisParser

from backend.utils import url_domain

from .api_model import APIModel


async def whois(hostname: str, timeout: int = 3):
    result = await asyncwhois.aio_whois_domain(hostname, timeout=timeout)
    parser = WhoisParser()
    return parser.parse(result.query_output, hostname=hostname)


class Whois(APIModel):
    registrar: str | None = Field(default=None)
    registrant_name: str | None = Field(default=None)
    registrant_email: str | None = Field(default=None)
    registrant_organization: str | None = Field(default=None)

    @classmethod
    async def parse_response(cls, response: requests.Response) -> "Whois":
        domain = url_domain(response.url)

        try:
            record = await whois(domain)
        except Exception:
            return cls()

        return cls(
            registrar=record.registrar,
            registrant_name=record.registrant.name,
            registrant_email=record.registrant.email,
            registrant_organization=record.registrant.organization,
        )
