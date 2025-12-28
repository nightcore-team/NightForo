from typing import Any
import aiohttp

from .errors import UnsupportedEndpointMethod, XenForoError

from .endpoints import endpoint_thread
from .endpoint import Endpoint, HTTPMethod

from .types.thread import Thread


class HTTPClient:
    async def _request(
        self, endpoint: Endpoint, method: HTTPMethod, **kwargs: Any
    ) -> Any:
        if method not in endpoint.supported_methods:
            raise UnsupportedEndpointMethod(method)

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method.value, endpoint.url, **kwargs
            ) as response:
                if response.ok:
                    payload = await response.json()

                    if (errors := payload.get("errors", None)) is not None:
                        raise XenForoError(errors)

                    return
                else:
                    raise XenForoError("")

    async def get_thread(self, thread_id: int) -> Thread:
        resp = await self._request(
            endpoint=endpoint_thread(thread_id), method=HTTPMethod.GET
        )

        thread_payload = resp.get("thread", None)

        return Thread.model_validate(thread_payload)
