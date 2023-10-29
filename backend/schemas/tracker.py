from pydantic import Field

from .api_model import APIModel


class Tracker(APIModel):
    google_adsense_id: str | None = Field(default=None)
    google_analytics_id: str | None = Field(default=None)
