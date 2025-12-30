from typing import List
from pydantic import BaseModel

from . import UserAlert


class AlertsGetResponse(BaseModel):
    alerts: List[UserAlert]
    pagination: pagination


class AlertSendResponse(BaseModel):
    success: bool


class AlertsMarkAllResponse(BaseModel):
    success: bool


class AlertMarkResponse(BaseModel):
    success: bool
