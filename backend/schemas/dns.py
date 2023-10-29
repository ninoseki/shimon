from pydantic import Field

from .api_model import APIModel


class A(APIModel):
    host: str
    ttl: int


class AAAA(A):
    pass


class CNAME(APIModel):
    cname: str
    ttl: int


class TXT(APIModel):
    text: str
    ttl: int


class DNS(APIModel):
    a: list[A] = Field(default_factory=list)
    aaaa: list[AAAA] = Field(default_factory=list)
    cname: list[CNAME] = Field(default_factory=list)
    txt: list[TXT] = Field(default_factory=list)
