from typing import Any, Set

from enum import Enum


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class Endpoint:
    def __init__(
        self,
        url: str,
        supported_methods: Set[HTTPMethod],
    ) -> None:
        self.url = url
        self.supported_methods = supported_methods

    def __add__(self, other: Any):
        if isinstance(other, str):
            return self.url + other
        else:
            return NotImplemented


def create_endpoint(url: str, *supported_methods: HTTPMethod):
    return Endpoint(url=url, supported_methods=set(supported_methods))
