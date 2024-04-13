import sys

from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME: str = config("PROJECT_NAME", default="shimon")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
TESTING: bool = config("TESTING", cast=bool, default=False)

LOG_FILE = config("LOG_FILE", default=sys.stderr)
LOG_LEVEL: str = config("LOG_LEVEL", cast=str, default="DEBUG")
LOG_BACKTRACE: bool = config("LOG_BACKTRACE", cast=bool, default=True)


SHODAN_API_KEY: Secret | None = config("SHODAN_API_KEY", cast=Secret, default=None)
CENSYS_APP_ID: Secret | None = config("CENSYS_APP_ID", cast=Secret, default=None)
CENSYS_SECRET: Secret | None = config("CENSYS_SECRET", cast=Secret, default=None)
