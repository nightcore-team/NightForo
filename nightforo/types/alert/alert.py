from enum import Enum

from pydantic import BaseModel

from ...types.content_type import ContentTypeEnum
from ..user import User

__all__ = ("AlertActionTypeEnum", "UserAlert")


class AlertActionTypeEnum(Enum):
    INSERT = "insert"
    AWARD = "award"
    TROPHY = "trophy"


class UserAlert(BaseModel):
    action: AlertActionTypeEnum
    alert_id: int
    alert_text: str
    alert_url: str
    alerted_user_id: int
    auto_read: bool
    content_id: int
    content_type: ContentTypeEnum
    event_date: int
    read_date: int
    User: User
    user_id: int
    username: str
    view_date: int
