from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ..node import Node
from ..user import User
from ..vote_type import VoteTypeEnum


class Thread(BaseModel):
    username: str
    is_watching: Optional[
        bool
    ]  # If accessing as a user, true if they are watching this thread
    visitor_post_count: (
        Optional[
            int
        ]  # If accessing as a user, the number of posts they have made in this thread
    )
    is_unread: Optional[
        bool
    ]  # If accessing as a user, true if this thread is unread
    custom_fields: Dict[
        str, Any
    ]  # Key-value pairs of custom field values for this thread
    tags: List[str]
    prefix: Optional[
        str
    ]  # Present if this thread has a prefix. Printable name of the prefix.
    can_edit: bool
    can_edit_tags: bool
    can_reply: bool
    can_soft_delete: bool
    can_hard_delete: bool
    can_view_attachments: bool
    view_url: str
    is_first_post_pinned: bool
    highlighted_post_ids: List[int]
    is_search_engine_indexable: bool
    index_state: str  # Present for members with permission to change the search index state of this thread.
    Forum: Optional[
        Node
    ]  # If requested by context, the forum this thread was posted in.
    vote_score: int  # The content's vote score (if supported)
    can_content_vote: bool  # True if the viewing user can vote on this content
    allowed_content_vote_types: List[
        str
    ]  # List of content vote types allowed on this content
    is_content_voted: (
        bool  # True if the viewing user has voted on this content
    )
    visitor_content_vote: Optional[
        VoteTypeEnum
    ]  # If the viewer reacted, the vote they case (up/down)
    thread_id: int
    node_id: int
    title: str
    reply_count: int
    view_count: int
    user_id: int
    post_date: int
    sticky: bool
    discussion_state: str
    discussion_open: bool
    discussion_type: str
    first_post_id: int
    last_post_date: int
    last_post_id: int
    last_post_user_id: int
    last_post_username: str
    first_post_reaction_score: int
    prefix_id: int
    User: User
