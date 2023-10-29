from pydantic import Field

from .resource import Resource


class HTML(Resource):
    title: str | None = Field(default=None)
