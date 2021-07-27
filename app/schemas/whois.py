from typing import Optional

import asyncwhois
import requests
from d8s_urls import url_domain
from fastapi_utils.api_model import APIModel
from whois_parser import WhoisParser


async def whois(hostname: str, timeout: int = 3):
    result = await asyncwhois.aio_lookup(hostname, timeout)
    parser = WhoisParser()
    return parser.parse(result.query_output, hostname=hostname)


class Whois(APIModel):
    registrar: Optional[str]
    registrant_name: Optional[str]
    registrant_email: Optional[str]
    registrant_organization: Optional[str]

    @classmethod
    async def build_from_response(cls, response: requests.Response) -> "Whois":
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
