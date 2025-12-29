from typing import List, Optional
from pydantic import BaseModel

from .attachment import Attachment
from .user import User
from .profile_post import ProfilePost


class ProfilePostComment(BaseModel):
    username: str
    message_parsed: str  # HTML parsed version of the message contents.
    can_edit: bool
    can_soft_delete: bool
    can_hard_delete: bool
    can_react: bool
    can_view_attachments: bool
    Attachments: List[
        Attachment
    ]  # 	 Attachments to this profile post, if it has any.
    ProfilePost: Optional[
        ProfilePost
    ]  #  If requested by context, the profile post this comment relates to.
    is_reacted_to: bool  # True if the viewing user has reacted to this content
    visitor_reaction_id: Optional[
        int
    ]  # If the viewer reacted, the ID of the reaction they used
    profile_post_comment_id: int
    profile_post_id: int
    user_id: int
    comment_date: int
    message: str
    message_state: str
    warning_message: str
    reaction_score: int
    User: User


class PostProfilePostCommentParams(BaseModel):
    profile_post_id: int
    message: str
    attachment_key: Optional[str] = None


class PostProfilePostCommentUpdateParams(BaseModel):
    message: str
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None
    attachment_key: Optional[str] = None


class DeleteProfilePostCommentParams(BaseModel):
    hard_delete: Optional[bool] = None
    reason: Optional[str] = None
    author_alert: Optional[bool] = None
    author_alert_reason: Optional[str] = None


class PostProfilePostCommentReactParams(BaseModel):
    reaction_id: int


class GetProfilePostCommentsParams(BaseModel):
    page: Optional[int] = None
    direction: Optional[str] = None
