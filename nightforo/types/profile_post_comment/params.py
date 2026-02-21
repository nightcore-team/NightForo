from typing import Optional

from pydantic import BaseModel, field_serializer

from ...types.direction import DirectionTypeEnum

__all__ = (
    "ProfilePostCommentCreateParams",
    "ProfilePostCommentDeleteParams",
    "ProfilePostCommentReactParams",
    "ProfilePostCommentUpdateParams",
    "ProfilePostCommentsGetParams",
)


class ProfilePostCommentCreateParams(BaseModel):
    profile_post_id: int
    message: str
    attachment_key: Optional[str] = None


class ProfilePostCommentUpdateParams(BaseModel):
    message: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None
    attachment_key: Optional[str] = None

    @field_serializer("author_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ProfilePostCommentDeleteParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None

    @field_serializer("author_alert", "hard_delete")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ProfilePostCommentReactParams(BaseModel):
    reaction_id: int


class ProfilePostCommentsGetParams(BaseModel):
    page: Optional[int] = None
    direction: Optional[DirectionTypeEnum] = None

    @field_serializer("direction")
    def serialize_type(self, v: DirectionTypeEnum):
        return v.value
