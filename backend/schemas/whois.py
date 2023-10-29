import asyncwhois
import requests
from asyncwhois import DomainLookup
from pydantic import Field

from backend.utils import url_domain

from .api_model import APIModel


async def whois(hostname: str, timeout: int = 3) -> DomainLookup:
    return await asyncwhois.aio_whois_domain(hostname, timeout=timeout)


class Whois(APIModel):
    registrar: str | None = Field(default=None)
    registrant_name: str | None = Field(default=None)
    registrant_email: str | None = Field(default=None)
    registrant_organization: str | None = Field(default=None)

    @classmethod
    async def parse_response(cls, response: requests.Response) -> "Whois":
        domain = url_domain(response.url)

        try:
            lookup = await whois(domain)
        except Exception:
            return cls()

        return cls(
            registrar=lookup.parser_output.get("registrar"),
            registrant_name=lookup.parser_output.get("registrant_name"),
            registrant_email=lookup.parser_output.get("registrant_email"),
            registrant_organization=lookup.parser_output.get("registrant_organization"),
        )
