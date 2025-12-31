from typing import List, Optional

from pydantic import BaseModel

from ..attachment import Attachment
from ..thread import Thread
from ..user import User

__all__ = ("Post",)


class Post(BaseModel):
    username: str
    is_first_post: bool
    is_last_post: bool
    is_unread: Optional[
        bool
    ]  # If accessing as a user, true if this post is unread
    message_parsed: str  # HTML parsed version of the message contents.
    can_edit: bool
    can_soft_delete: bool
    can_hard_delete: bool
    can_react: bool
    can_view_attachments: bool
    view_url: str
    Thread: Optional[
        Thread
    ]  # If requested by context, the thread this post is part of.
    Attachments: List[Attachment]  # Attachments to this post, if it has any.
    is_reacted_to: bool  # True if the viewing user has reacted to this content
    visitor_reaction_id: Optional[
        int
    ]  # If the viewer reacted, the ID of the reaction they used
    vote_score: Optional[int]  # The content's vote score (if supported)
    can_content_vote: bool  # True if the viewing user can vote on this content
    allowed_content_vote_types: List[
        str
    ]  # List of content vote types allowed on this content
    is_content_voted: (
        bool  # True if the viewing user has voted on this content
    )
    visitor_content_vote: Optional[
        str
    ]  # If the viewer reacted, the vote they case (up/down)
    post_id: int
    thread_id: int
    user_id: int
    post_date: int
    message: str
    message_state: str
    attach_count: int
    warning_message: str
    position: int
    last_edit_date: int
    reaction_score: int
    User: User
