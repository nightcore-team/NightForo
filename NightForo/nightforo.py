from typing import Optional

from .http import HTTPClient
from .types.thread import Thread


class NightForo:
    def __init__(self, http_client: HTTPClient) -> None:
        self._http = http_client

    async def get_thread(self, thread_id: int) -> Optional[Thread]:
        return await self._http.get_thread(thread_id)
