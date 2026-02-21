from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, field_serializer

from ...types.direction import DirectionTypeEnum
from ...types.thread_type import ThreadTypeEnum

__all__ = (
    "ForumGetParams",
    "ForumMarkReadParams",
    "ForumThreadsGetParams",
    "OrderField",
)


class OrderField(Enum):
    LAST_POST_DATE = "last_post_date"
    POST_DATE = "post_date"
    TITLE = "title"
    REPLY_COUNT = "reply_count"
    VIEW_COUNT = "view_count"
    VOTE_SCORE = "vote_score"
    FIRST_POST_REACTION_SCORE = "first_post_reaction_score"


class ForumGetParams(BaseModel):
    with_threads: Optional[bool] = None
    page: Optional[int] = None
    prefix_id: Optional[int] = None
    starter_id: Optional[int] = None
    last_days: Optional[int] = None
    unread: Optional[bool] = None
    thread_type: Optional[ThreadTypeEnum] = None
    order: Optional[OrderField] = None
    direction: Optional[DirectionTypeEnum] = None

    @field_serializer("with_threads", "unread")
    def serialize_bool(self, v: bool):
        return 1 if v else 0

    @field_serializer("direction", "thread_type", "order")
    def serialize_type(
        self, v: Union[ThreadTypeEnum, DirectionTypeEnum, OrderField]
    ):
        return v.value


class ForumMarkReadParams(BaseModel):
    date: int


class ForumThreadsGetParams(BaseModel):
    page: Optional[int] = None
    prefix_id: Optional[int] = None
    starter_id: Optional[int] = None
    last_days: Optional[int] = None
    unread: Optional[bool] = None
    thread_type: Optional[str] = None
    order: Optional[str] = None
    direction: Optional[DirectionTypeEnum] = None

    @field_serializer("unread")
    def serialize_bool(self, v: bool):
        return 1 if v else 0

    @field_serializer("direction")
    def serialize_type(self, v: DirectionTypeEnum):
        return v.value
