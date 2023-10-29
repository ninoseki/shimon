from pydantic import Field

from .api_model import APIModel


class Whois(APIModel):
    registrar: str | None = Field(default=None)
    registrant_name: str | None = Field(default=None)
    registrant_email: str | None = Field(default=None)
    registrant_organization: str | None = Field(default=None)
