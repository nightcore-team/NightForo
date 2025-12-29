from typing import List, Optional

from pydantic import BaseModel


class UserAlert(BaseModel): ...


class AlertsGetResponse(BaseModel):
    alerts: List[UserAlert]
    pagination: pagination


class AlertsGetParams(BaseModel):
    page: Optional[int] = None
    cutoff: Optional[int] = None
    unviewed: Optional[bool] = None
    unread: Optional[bool] = None


class AlertSendResponse(BaseModel):
    success: bool


class AlertSendParams(BaseModel):
    to_user_id: int
    alert: str
    from_user_id: Optional[int] = None
    link_url: Optional[str] = None
    link_title: Optional[str] = None


class AlertsMarkAllParams(BaseModel):
    read: Optional[bool] = None
    viewed: Optional[bool] = None


class PostAlertMarkParams(BaseModel):
    read: Optional[bool] = None
    unread: Optional[bool] = None
    viewed: Optional[bool] = None
