from typing import Any, BinaryIO, Dict, Optional

from pydantic import BaseModel


class PostMeUpdateParams(BaseModel):
    option: Optional[Dict[str, Any]] = None
    profile: Optional[Dict[str, str]] = None
    privacy: Optional[Dict[str, str]] = None
    visible: Optional[bool] = None
    activity_visible: Optional[bool] = None
    timezone: Optional[str] = None
    custom_title: Optional[str] = None
    custom_fields: Optional[Dict[str, str]] = None


class PostMeAvatarParams(BaseModel):
    avatar: BinaryIO  # File upload


class PostMeEmailParams(BaseModel):
    current_password: str
    email: str


class PostMePasswordParams(BaseModel):
    current_password: str
    new_password: str
