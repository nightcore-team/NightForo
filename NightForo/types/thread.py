from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .post import Post
from .vote_type import VoteType
from .node import Node
from .user import User


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
    is_unread: Optional[bool]  # If accessing as a user, true if this thread is unread
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
    is_content_voted: bool  # True if the viewing user has voted on this content
    visitor_content_vote: Optional[
        str
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


class GetThreadsParams(BaseModel):
    page: Optional[int] = None
    prefix_id: Optional[int] = None
    starter_id: Optional[int] = None
    last_days: Optional[int] = None
    unread: Optional[bool] = None
    thread_type: Optional[str] = None
    order: Optional[str] = None
    direction: Optional[str] = None


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


class ThreadGetParams(BaseModel):
    with_posts: Optional[bool] = None
    page: Optional[int] = None
    with_first_post: Optional[bool] = None
    with_last_post: Optional[bool] = None
    order: Optional[str] = None


class PostThreadUpdateParams(BaseModel):
    prefix_id: Optional[int] = None
    title: Optional[str] = None
    discussion_open: Optional[bool] = None
    sticky: Optional[bool] = None
    custom_fields: Optional[Dict[str, str]] = None
    add_tags: Optional[List[str]] = None
    remove_tags: Optional[List[str]] = None


class DeleteThreadParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    starter_alert: Optional[bool] = None
    starter_alert_reason: Optional[str] = None


class PostThreadChangeTypeParams(BaseModel):
    new_thread_type_id: str


class PostThreadMarkReadParams:
    date: Optional[int] = None


class PostThreadMoveParams(BaseModel):
    target_node_id: int
    prefix_id: Optional[int] = None
    title: Optional[str] = None
    notify_watchers: Optional[bool] = None
    starter_alert: Optional[bool] = None
    starter_alert_reason: Optional[str] = None


class GetThreadPostsParams(BaseModel):
    page: Optional[int] = None
    order: Optional[str] = None


class PostThreadVoteParams(BaseModel):
    type: VoteType


class ThreadCreateResponse(BaseModel):
    success: bool
    thread: Thread


class GetThreadResponse(BaseModel):
    thread: Thread
    first_unread: Optional[Post]
    first_post: Optional[Post]
    last_post: Optional[Post]
    pinned_post: Optional[Post]
    highlighted_posts: List[Optional[List[Post]]]
    posts: List[Post]
    pagination: pagination
