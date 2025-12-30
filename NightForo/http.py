from typing import Any, Optional
import aiohttp
from pydantic import BaseModel

from .errors import UnsupportedEndpointMethod, XenForoError

from .endpoints import (
    endpoint_thread,
    endpoint_threads,
    endpoint_stats,
    endpoint_alerts,
)
from .endpoint import Endpoint, HTTPMethod

from .types.thread.params import ThreadGetParams, ThreadCreateParams
from .types.alert.params import AlertsGetParams, AlertSendParams


class HTTPClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    async def _request(
        self, endpoint: Endpoint, method: HTTPMethod, params: Optional[BaseModel] = None
    ) -> Any:
        headers = {}
        req = {}

        headers["XF-Api-Key"] = self.api_key
        headers["Content-Type"] = "application/json"

        req["headers"] = headers

        if params is not None:
            req["json"] = params.model_dump()

        if method not in endpoint.supported_methods:
            raise UnsupportedEndpointMethod(method)

        async with aiohttp.ClientSession() as session:
            async with session.request(method.value, endpoint.url, **req) as response:
                if response.ok:
                    try:
                        payload = await response.json()
                    except aiohttp.ContentTypeError:
                        raise XenForoError(
                            f"Response is not JSON. Status: {response.status}"
                        )

                    if (errors := payload.get("errors", None)) is not None:
                        raise XenForoError(errors)

                    return payload
                else:
                    raise XenForoError("")

    async def get_alerts(self, params: AlertsGetParams) -> Any:
        return await self._request(
            endpoint=endpoint_alerts, method=HTTPMethod.GET, params=params
        )

    async def send_alert(self, params: AlertSendParams) -> Any:
        return await self._request(
            endpoint=endpoint_alerts, method=HTTPMethod.POST, params=params
        )

    async def get_stats(self):
        return await self._request(endpoint=endpoint_stats, method=HTTPMethod.GET)

    async def get_thread(self, thread_id: int, params: ThreadGetParams) -> Any:
        return await self._request(
            endpoint=endpoint_thread(thread_id), method=HTTPMethod.GET, params=params
        )

    async def create_thread(self, params: ThreadCreateParams) -> Any:
        return await self._request(
            endpoint=endpoint_threads, method=HTTPMethod.POST, params=params
        )
