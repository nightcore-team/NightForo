from .errors import NoApiKeyProvided

from .http import HTTPClient
from .types.thread.response import (
    ThreadGetResponse,
    ThreadCreateResponse,
)
from .types.thread.params import (
    ThreadGetParams,
    ThreadCreateParams,
)
from .types.stats.response import StatsResponse
from .types.alert.params import (
    AlertsGetParams,
    AlertSendParams,
)
from .types.alert.response import (
    AlertsGetResponse,
    AlertSendResponse,
)


class Client:
    def __init__(self, api_key: str) -> None:
        if api_key == "":
            raise NoApiKeyProvided()

        self._http = HTTPClient(api_key)

    async def get_alerts(self, params: AlertsGetParams) -> AlertsGetResponse:
        """GET alerts/ - Gets the API user's list of alerts

        Parameters
        ----------
        page : int
        cutoff : int
            Unix timestamp of oldest alert to include. Note that unread or unviewed alerts are always included.
        unviewed : bool
            If true, gets only unviewed alerts. Unviewed alerts have not been seen (in the standard UI).
        unread : bool
            If true, gets only unread alerts. Unread alerts may have been seen but the content they relate to has not been viewed.
        """

        payload = await self._http.get_alerts(params)

        return AlertsGetResponse.model_validate(payload)

    async def send_alert(self, params: AlertSendParams) -> AlertSendResponse:
        """POST alerts/ - Sends an alert to the specified user. Only available to super user keys.

        Parameters
        ----------
        to_user_id : int
            ID of the user to receive the alert.
        alert : str
            Text of the alert. May use the placeholder "{link}" to have
            the link automatically inserted.
        from_user_id : Optional[int], default=None
            If provided, the user to send the alert from. Otherwise,
            uses the current API user. May be 0 for an anonymous alert.
        link_url : Optional[str], default=None
            URL user will be taken to when the alert is clicked.
        link_title : Optional[str], default=None
            Text of the link URL that will be displayed. If no placeholder
            is present in the alert, will be automatically appended.
        """

        payload = await self._http.send_alert(params)

        return AlertSendResponse.model_validate(payload)

    async def get_stats(self) -> StatsResponse:
        """GET stats/ - Gets site statistics and general activity information."""

        payload = await self._http.get_stats()

        return StatsResponse.model_validate(payload)

    async def get_thread(
        self, thread_id: int, params: ThreadGetParams
    ) -> ThreadGetResponse:
        payload = await self._http.get_thread(thread_id, params)

        return ThreadGetResponse.model_validate(payload)

    async def create_thread(self, params: ThreadCreateParams) -> ThreadCreateResponse:
        payload = await self._http.create_thread(params)

        return ThreadCreateResponse.model_validate(payload)
