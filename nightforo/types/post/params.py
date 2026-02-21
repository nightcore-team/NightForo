from typing import Optional

from pydantic import BaseModel, field_serializer

from ..vote_type import VoteTypeEnum

__all__ = (
    "PostCreateParams",
    "PostDeleteParams",
    "PostReactParams",
    "PostUpdateParams",
    "PostVoteParams",
)


class PostCreateParams(BaseModel):
    thread_id: int
    message: str
    attachment_key: Optional[str] = None


class PostUpdateParams(BaseModel):
    message: str
    silent: Optional[bool] = None
    clear_edit: Optional[bool] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None
    attachment_key: Optional[str] = None

    @field_serializer("silent", "clear_edit", "author_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class PostDeleteParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None

    @field_serializer("hard_delete", "author_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class PostReactParams(BaseModel):
    reaction_id: int


class PostVoteParams(BaseModel):
    type: VoteTypeEnum

    @field_serializer("type")
    def serialize_type(self, v: VoteTypeEnum):
        return v.value
