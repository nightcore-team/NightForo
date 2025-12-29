from typing import List, Optional
from pydantic import BaseModel

from .user import User
from .attachment import Attachment
from .profile_post_comment import ProfilePostComment


class ProfilePost(BaseModel):
    username: str
    message_parsed: str  # HTML parsed version of the message contents.
    can_edit: bool
    can_soft_delete: bool
    can_hard_delete: bool
    can_react: bool
    can_view_attachments: bool
    view_url: str
    ProfileUser: (
        Optional[
            User
        ]  # If requested by context, the user this profile post was left for.
    )
    Attachments: List[Attachment]  # Attachments to this profile post, if it has any.
    LatestComments: List[
        ProfilePostComment
    ]  # If requested, the most recent comments on this profile post.
    is_reacted_to: bool  # True if the viewing user has reacted to this content
    visitor_reaction_id: Optional[
        int
    ]  # If the viewer reacted, the ID of the reaction they used
    profile_post_id: int
    profile_user_id: int
    user_id: int
    post_date: int
    message: str
    message_state: str
    warning_message: str
    comment_count: int
    first_comment_date: int
    last_comment_date: int
    reaction_score: int
    User: User


class PostProfilePostParams(BaseModel):
    user_id: int
    message: str
    attachment_key: Optional[str] = None


class GetProfilePostParams(BaseModel):
    with_comments: Optional[bool] = None
    page: Optional[int] = None
    direction: Optional[str] = None


class PostProfilePostUpdateParams(BaseModel):
    message: str
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None
    attachment_key: Optional[str] = None


class DeleteProfilePostParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None


class PostProfilePostReactParams(BaseModel):
    reaction_id: int
