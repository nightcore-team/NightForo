from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field

from ...types.discussion_state import DiscussionStateEnum
from ..user import User
from ..vote_type import VoteTypeEnum

if TYPE_CHECKING:
    from ..node import Node

__all__ = ("Thread",)


class Thread(BaseModel):
    thread_id: int
    node_id: int
    title: str
    username: str
    user_id: int
    user: User = Field(alias="User")
    is_watching: bool | None = None
    visitor_post_count: int | None = None
    is_unread: bool | None = None
    custom_fields: dict[str, Any]
    tags: list[str] | None = None
    prefix: str | None = None
    can_edit: bool
    can_edit_tags: bool
    can_reply: bool
    can_soft_delete: bool
    can_hard_delete: bool
    can_view_attachments: bool
    view_url: str
    is_first_post_pinned: bool
    highlighted_post_ids: list[int]
    is_search_engine_indexable: bool | None = None
    index_state: str | None = None
    forum: Node | None = Field(alias="Forum", default=None)
    vote_score: int | None = None
    can_content_vote: bool | None = None
    allowed_content_vote_types: list[str] | None = None
    is_content_voted: bool | None = None
    visitor_content_vote: VoteTypeEnum | None = None
    reply_count: int
    view_count: int
    post_date: int
    sticky: bool
    discussion_state: DiscussionStateEnum
    discussion_open: bool
    discussion_type: str
    first_post_id: int
    last_post_date: int
    last_post_id: int
    last_post_user_id: int
    last_post_username: str
    first_post_reaction_score: int
    prefix_id: int
