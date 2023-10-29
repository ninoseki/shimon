import typing
from abc import ABC, abstractmethod


class AbstractService(ABC):
    @abstractmethod
    async def call(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        raise NotImplementedError()
