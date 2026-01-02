from typing import TYPE_CHECKING, Any, Dict, List, Optional

from pydantic import BaseModel, Field

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
    user: Optional[User] = Field(alias="User", default=None)
    is_watching: Optional[bool] = None
    visitor_post_count: Optional[int] = None
    is_unread: Optional[bool] = None
    custom_fields: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None
    prefix: Optional[str] = None
    can_edit: Optional[bool] = None
    can_edit_tags: Optional[bool] = None
    can_reply: Optional[bool] = None
    can_soft_delete: Optional[bool] = None
    can_hard_delete: Optional[bool] = None
    can_view_attachments: Optional[bool] = None
    view_url: Optional[str] = None
    is_first_post_pinned: Optional[bool] = None
    highlighted_post_ids: Optional[List[int]] = None
    is_search_engine_indexable: Optional[bool] = None
    index_state: Optional[str] = None
    Forum: Optional[Node] = None
    vote_score: Optional[int] = None
    can_content_vote: Optional[bool] = None
    allowed_content_vote_types: Optional[List[str]] = None
    is_content_voted: Optional[bool] = None
    visitor_content_vote: Optional[VoteTypeEnum] = None
    reply_count: Optional[int] = None
    view_count: Optional[int] = None
    post_date: Optional[int] = None
    sticky: Optional[bool] = None
    discussion_state: Optional[str] = None
    discussion_open: Optional[bool] = None
    discussion_type: Optional[str] = None
    first_post_id: Optional[int] = None
    last_post_date: Optional[int] = None
    last_post_id: Optional[int] = None
    last_post_user_id: Optional[int] = None
    last_post_username: Optional[str] = None
    first_post_reaction_score: Optional[int] = None
    prefix_id: Optional[int] = None
