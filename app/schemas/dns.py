from typing import Any, List, Literal, Optional, cast

import aiodns
import requests
from d8s_urls import url_domain
from fastapi_utils.api_model import APIModel
from pycares import (
    ares_query_a_result,
    ares_query_aaaa_result,
    ares_query_cname_result,
    ares_query_txt_result,
)

QUERY_TYPES = Literal["A", "AAAA", "CNAME", "TXT"]


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


async def query(name: str, query_type: QUERY_TYPES):
    try:
        resolver = aiodns.DNSResolver()
        records = await resolver.query(name, query_type)

        if not isinstance(records, list):
            records = [records]

        return cast(List[Any], records)
    except aiodns.error.DNSError:
        return None


async def query_a_records(name: str):
    records = await query(name, "A")
    if records is None:
        return None

    records = cast(List[ares_query_a_result], records)

    models = []
    for record in records:
        models.append(A(host=record.host, ttl=record.ttl))

    return models


async def query_aaaa_records(name: str):
    records = await query(name, "AAAA")
    if records is None:
        return None

    records = cast(List[ares_query_aaaa_result], records)

    models = []
    for record in records:
        models.append(AAAA(host=record.host, ttl=record.ttl))

    return models


async def query_cname_records(name: str):
    records = await query(name, "CNAME")
    if records is None:
        return None

    records = cast(List[ares_query_cname_result], records)

    models = []
    for record in records:
        models.append(CNAME(cname=record.cname, ttl=record.ttl))

    return models


async def query_txt_records(name: str):
    records = await query(name, "TXT")
    if records is None:
        return None

    records = cast(List[ares_query_txt_result], records)

    models = []
    for record in records:
        models.append(TXT(text=record.text, ttl=record.ttl))

    return models


class DNS(APIModel):
    a: Optional[List[A]]
    aaaa: Optional[List[AAAA]]
    cname: Optional[List[CNAME]]
    txt: Optional[List[TXT]]

    @classmethod
    async def build_from_response(cls, response: requests.Response) -> "DNS":
        domain = url_domain(response.url)

        a = await query_a_records(domain)
        aaaa = await query_aaaa_records(domain)
        cname = await query_cname_records(domain)
        txt = await query_txt_records(domain)

        return cls(a=a, aaaa=aaaa, cname=cname, txt=txt)
