from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from ...types.groups import ArzGuardGroupsIdsEnum

__all__ = (
    "DateOfBirth",
    "Option",
    "Privacy",
    "Profile",
    "ProfileAvatars",
    "ProfileBanners",
    "ProfilePrivacyLevelEnum",
    "User",
    "UserCustomFields",
    "UserStateEnum",
)


class DateOfBirth(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None


class ProfileAvatars(BaseModel):
    o: Optional[str] = None
    h: Optional[str] = None
    l: Optional[str] = None  # noqa: E741
    m: Optional[str] = None
    s: Optional[str] = None


class ProfileBanners(BaseModel):
    l: Optional[str] = None  # noqa: E741
    m: Optional[str] = None


class UserCustomFields(BaseModel):
    server: Optional[str] = None
    bot_owner: Optional[str] = None
    gender: Optional[str] = None
    occupation: Optional[str] = None
    vk: Optional[str] = None
    discord: Optional[str] = None
    telegram: Optional[str] = Field(default=None, alias="Telegram")


class Option(BaseModel):
    creation_watch_state: Optional[str] = None
    interaction_watch_state: Optional[str] = None
    content_show_signature: Optional[bool] = None
    email_on_conversation: Optional[bool] = None
    push_on_conversation: Optional[bool] = None
    receive_admin_email: Optional[bool] = None
    show_dob_year: Optional[bool] = None
    show_dob_date: Optional[bool] = None


class Profile(BaseModel):
    location: Optional[str] = None
    website: Optional[str] = None
    about: Optional[str] = None
    signature: Optional[str] = None


class Privacy(BaseModel):
    allow_view_profile: Optional[str] = None
    allow_post_profile: Optional[str] = None
    allow_receive_news_feed: Optional[str] = None
    allow_send_personal_conversation: Optional[str] = None
    allow_view_identities: Optional[str] = None


class UserStateEnum(Enum):
    VALID = "valid"
    EMAIL_CONFIRM = "email_confirm"
    EMAIL_CONFIRM_EDIT = "email_confirm_edit"
    EMAIL_BOUNCE = "email_bounce"
    MODERATED = "moderated"
    REJECTED = "rejected"
    DISABLED = "disabled"


class ProfilePrivacyLevelEnum(Enum):
    MEMBERS = "members"
    EVERYONE = "everyone"
    NONE = "none"


class User(BaseModel):
    user_id: int
    username: str

    activity_visible: Optional[bool] = None
    age: Optional[int] = None
    alert_optout: Optional[List[str]] = None
    allow_post_profile: Optional[ProfilePrivacyLevelEnum] = None
    allow_receive_news_feed: Optional[ProfilePrivacyLevelEnum] = None
    allow_send_personal_conversation: Optional[ProfilePrivacyLevelEnum] = None
    allow_view_identities: Optional[ProfilePrivacyLevelEnum] = None
    allow_view_profile: Optional[ProfilePrivacyLevelEnum] = None
    avatar_urls: Optional[ProfileAvatars] = None
    profile_banner_urls: Optional[ProfileBanners] = None
    can_ban: bool
    can_converse: bool
    can_edit: bool
    can_follow: bool
    can_ignore: bool
    can_post_profile: bool
    can_view_profile: bool
    can_view_profile_posts: bool
    can_warn: bool
    content_show_signature: Optional[bool] = None
    creation_watch_state: Optional[str] = None
    custom_fields: Optional[UserCustomFields] = None
    custom_title: Optional[str] = None
    dob: Optional[DateOfBirth] = None
    email: Optional[str] = None
    email_on_conversation: Optional[bool] = None
    gravatar: Optional[str] = None
    interaction_watch_state: Optional[str] = None
    is_admin: Optional[bool] = None
    is_banned: Optional[bool] = None
    is_discouraged: Optional[bool] = None
    is_followed: Optional[bool] = None
    is_ignored: Optional[bool] = None
    is_moderator: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    last_activity: Optional[int] = None
    location: Optional[str] = None
    push_on_conversation: Optional[bool] = None
    push_optout: Optional[List[str]] = None
    receive_admin_email: Optional[bool] = None
    secondary_group_ids: Optional[List[ArzGuardGroupsIdsEnum]] = None
    show_dob_date: Optional[bool] = None
    show_dob_year: Optional[bool] = None
    signature: Optional[str] = None
    timezone: Optional[str] = None
    use_tfa: Optional[bool] = None
    user_group_id: Optional[int] = None
    user_state: Optional[UserStateEnum] = None

    user_title: Optional[Union[str, bool]] = None

    visible: Optional[bool] = None
    warning_points: Optional[int] = None
    website: Optional[str] = None
    view_url: str
    message_count: int
    question_solution_count: int
    register_date: int
    trophy_points: int
    is_staff: bool
    reaction_score: int
    vote_score: int
