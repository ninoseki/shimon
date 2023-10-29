import asyncwhois
import httpx

from backend import schemas

from .abstract import AbstractService


class Whois(AbstractService):
    async def call(
        self, response: httpx.Response, *, timeout: int = 5
    ) -> schemas.Whois:
        lookup = await asyncwhois.aio_whois_domain(response.url.host, timeout=timeout)
        return schemas.Whois(
            registrar=lookup.parser_output.get("registrar"),
            registrant_name=lookup.parser_output.get("registrant_name"),
            registrant_email=lookup.parser_output.get("registrant_email"),
            registrant_organization=lookup.parser_output.get("registrant_organization"),
        )
