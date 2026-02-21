from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, field_serializer

from ...types.direction import DirectionTypeEnum
from ...types.thread_type import ThreadTypeEnum
from ..vote_type import VoteTypeEnum

__all__ = (
    "OrderField",
    "ThreadChangeTypeParams",
    "ThreadCreateParams",
    "ThreadDeleteParams",
    "ThreadGetParams",
    "ThreadMarkReadParams",
    "ThreadMoveParams",
    "ThreadPostsGetParams",
    "ThreadUpdateParams",
    "ThreadVoteParams",
    "ThreadsGetParams",
)


class OrderField(Enum):
    LAST_POST_DATE = "last_post_date"
    POST_DATE = "post_date"
    TITLE = "title"
    REPLY_COUNT = "reply_count"
    VIEW_COUNT = "view_count"
    VOTE_SCORE = "vote_score"
    FIRST_POST_REACTION_SCORE = "first_post_reaction_score"


class ThreadsGetParams(BaseModel):
    page: Optional[int] = None
    prefix_id: Optional[int] = None
    starter_id: Optional[int] = None
    last_days: Optional[int] = None
    unread: Optional[bool] = None
    thread_type: Optional[ThreadTypeEnum] = None
    order: Optional[OrderField] = None
    direction: Optional[DirectionTypeEnum] = None

    @field_serializer("unread")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ThreadCreateParams(BaseModel):
    node_id: int
    title: str
    message: str
    discussion_type: Optional[str] = None
    prefix_id: Optional[int] = None
    tags: Optional[List[str]] = None
    custom_fields: Optional[Dict[str, Any]] = None
    discussion_open: Optional[bool] = None
    sticky: Optional[bool] = None
    attachment_key: Optional[str] = None

    @field_serializer("discussion_open", "sticky")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ThreadGetParams(BaseModel):
    with_posts: Optional[bool] = None
    page: Optional[int] = None
    with_first_post: Optional[bool] = None
    with_last_post: Optional[bool] = None
    order: Optional[str] = None

    @field_serializer("with_posts", "with_last_post", "with_first_post")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ThreadUpdateParams(BaseModel):
    prefix_id: Optional[int] = None
    title: Optional[str] = None
    discussion_open: Optional[bool] = None
    sticky: Optional[bool] = None
    custom_fields: Optional[Dict[str, str]] = None
    add_tags: Optional[List[str]] = None
    remove_tags: Optional[List[str]] = None

    @field_serializer("discussion_open", "sticky")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ThreadDeleteParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    starter_alert: Optional[bool] = None
    starter_alert_reason: Optional[str] = None

    @field_serializer("hard_delete", "starter_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ThreadChangeTypeParams(BaseModel):
    new_thread_type_id: ThreadTypeEnum

    @field_serializer("new_thread_type_id")
    def serialize_type(self, v: ThreadTypeEnum):
        return v.value


class ThreadMarkReadParams(BaseModel):
    date: int


class ThreadMoveParams(BaseModel):
    target_node_id: int
    prefix_id: Optional[int] = None
    title: Optional[str] = None
    notify_watchers: Optional[bool] = None
    starter_alert: Optional[bool] = None
    starter_alert_reason: Optional[str] = None

    @field_serializer("notify_watchers", "starter_alert")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ThreadPostsGetParams(BaseModel):
    page: Optional[int] = None
    order: Optional[str] = None


class ThreadVoteParams(BaseModel):
    type: VoteTypeEnum

    @field_serializer("type")
    def serialize_type(self, v: ThreadTypeEnum):
        return v.value
