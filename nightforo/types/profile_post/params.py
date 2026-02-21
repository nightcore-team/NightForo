from typing import Optional

from pydantic import BaseModel, field_serializer

from ...types.direction import DirectionTypeEnum

__all__ = (
    "ProfilePostCreateParams",
    "ProfilePostDeleteParams",
    "ProfilePostGetParams",
    "ProfilePostReactParams",
    "ProfilePostUpdateParams",
)


class ProfilePostCreateParams(BaseModel):
    user_id: int
    message: str
    attachment_key: Optional[str] = None


class ProfilePostGetParams(BaseModel):
    with_comments: Optional[bool] = None
    page: Optional[int] = None
    direction: Optional[DirectionTypeEnum] = None

    @field_serializer("with_comments")
    def serialize_bool(self, v: bool):
        return 1 if v else 0

    @field_serializer("direction")
    def serialize_type(self, v: DirectionTypeEnum):
        return v.value


class ProfilePostUpdateParams(BaseModel):
    message: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None
    attachment_key: Optional[str] = None

    @field_serializer("author_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ProfilePostDeleteParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None

    @field_serializer("hard_delete", "author_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ProfilePostReactParams(BaseModel):
    reaction_id: int
