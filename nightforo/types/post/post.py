from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from ...types.discussion_state import DiscussionStateEnum
from ..attachment import Attachment
from ..user import User

if TYPE_CHECKING:
    from ..thread import Thread

__all__ = ("Post",)


class Post(BaseModel):
    post_id: int
    thread_id: int
    user_id: int
    username: str
    message: str
    user: User | None = Field(alias="User", default=None)

    is_first_post: bool
    is_last_post: bool
    is_unread: bool
    message_parsed: str | None = None
    can_edit: bool
    can_soft_delete: bool
    can_hard_delete: bool
    can_react: bool
    can_view_attachments: bool | None = None
    view_url: str
    thread: Thread | None = Field(alias="Thread", default=None)
    attachments: list[Attachment] | None = Field(
        alias="Attachments", default=None
    )
    is_reacted_to: bool
    visitor_reaction_id: int | None = None
    vote_score: int | None = None
    can_content_vote: bool | None = None
    allowed_content_vote_types: list[str] | None = None
    is_content_voted: bool | None = None
    visitor_content_vote: str | None = None
    post_date: int
    message_state: DiscussionStateEnum
    attach_count: int
    warning_message: str
    position: int
    last_edit_date: int
    reaction_score: int
