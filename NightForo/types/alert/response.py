from typing import List
from pydantic import BaseModel

from . import UserAlert
from ..pagination import Pagination


class AlertsGetResponse(BaseModel):
    alerts: List[UserAlert]
    pagination: Pagination


class AlertSendResponse(BaseModel):
    success: bool


class AlertsMarkAllResponse(BaseModel):
    success: bool


class AlertGetResponse(BaseModel):
    alert: UserAlert


class AlertMarkResponse(BaseModel):
    success: bool
