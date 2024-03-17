import functools
import typing

import aiodns
import aiometer
import httpx
from pycares import (
    ares_query_a_result,
    ares_query_aaaa_result,
    ares_query_cname_result,
    ares_query_txt_result,
)
from returns.future import future_safe
from returns.unsafe import unsafe_perform_io

from backend import schemas
from backend.schemas.dns import AAAA, CNAME, TXT, A
from backend.utils import decode_str_byte

from .abstract import AbstractService

QUERY_TYPES = typing.Literal["A", "AAAA", "CNAME", "TXT"]


@future_safe
async def safe_query(
    name: str, query_type: QUERY_TYPES, resolver: aiodns.DNSResolver | None = None
) -> list[typing.Any]:
    resolver = resolver or aiodns.DNSResolver()
    records = await resolver.query(name, query_type)

    if not isinstance(records, list):
        records = [records]

    return typing.cast(list[typing.Any], records)


async def query(name: str, query_type: QUERY_TYPES) -> list[typing.Any]:
    return unsafe_perform_io((await safe_query(name, query_type)).value_or([]))


async def query_a_records(name: str) -> list[A]:
    records = await query(name, "A")
    records = typing.cast(list[ares_query_a_result], records)
    return [A(host=decode_str_byte(record.host), ttl=record.ttl) for record in records]


async def query_aaaa_records(name: str) -> list[AAAA]:
    records = await query(name, "AAAA")
    records = typing.cast(list[ares_query_aaaa_result], records)
    return [
        AAAA(host=decode_str_byte(record.host), ttl=record.ttl) for record in records
    ]


async def query_cname_records(name: str) -> list[CNAME]:
    records = await query(name, "CNAME")
    records = typing.cast(list[ares_query_cname_result], records)
    return [
        CNAME(cname=decode_str_byte(record.cname), ttl=record.ttl) for record in records
    ]


async def query_txt_records(name: str) -> list[TXT]:
    records = await query(name, "TXT")
    records = typing.cast(list[ares_query_txt_result], records)
    return [
        TXT(text=decode_str_byte(record.text), ttl=record.ttl) for record in records
    ]


class DNS(AbstractService):
    async def call(self, response: httpx.Response) -> schemas.DNS:
        tasks = [
            functools.partial(query_a_records, response.url.host),
            functools.partial(query_aaaa_records, response.url.host),
            functools.partial(query_cname_records, response.url.host),
            functools.partial(query_txt_records, response.url.host),
        ]
        a, aaaa, cname, txt = await aiometer.run_all(tasks)
        return schemas.DNS(a=a, aaaa=aaaa, cname=cname, txt=txt)
