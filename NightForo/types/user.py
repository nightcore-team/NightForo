from typing import Any, BinaryIO, Dict, List, Optional

from pydantic import BaseModel


class DateOfBirth(BaseModel):
    year: int
    month: int
    day: int


class ProfileAvatars(BaseModel):
    o: str
    h: str
    l: str  # noqa: E741
    m: str
    s: str


class ProfileBanners(BaseModel):
    l: str  # noqa: E741
    m: str


class User(BaseModel):
    activity_visible: bool
    age: Optional[int]  # The user's current age. Only included if available.
    alert_optout: List[str]
    allow_post_profile: str
    allow_receive_news_feed: str
    allow_send_personal_conversation: str
    allow_view_identities: str
    allow_view_profile: str
    avatar_urls: ProfileAvatars  # Maps from size types to URL.
    profile_banner_urls: ProfileBanners  # Maps from size types to URL.
    can_ban: bool
    can_converse: bool
    can_edit: bool
    can_follow: bool
    can_ignore: bool
    can_post_profile: bool
    can_view_profile: bool
    can_view_profile_posts: bool
    can_warn: bool
    content_show_signature: bool
    creation_watch_state: str
    custom_fields: Dict[str, Any]  # Map of custom field keys and values.
    custom_title: Optional[
        str
    ]  # Will have a value if a custom title has been specifically set; prefer user_title instead.
    dob: DateOfBirth  # Date of birth with year, month and day keys.
    email: str
    email_on_conversation: bool
    gravatar: str
    interaction_watch_state: bool
    is_admin: bool
    is_banned: bool
    is_discouraged: bool
    is_followed: Optional[
        bool
    ]  # True if the visitor is following this user. Only included if visitor is not a guest.
    is_ignored: Optional[
        bool
    ]  # True if the visitor is ignoring this user. Only included if visitor is not a guest.
    is_moderator: bool
    is_super_admin: bool
    last_activity: Optional[
        int
    ]  # Unix timestamp of user's last activity, if available.
    location: str
    push_on_conversation: bool
    push_optout: List[str]
    receive_admin_email: bool
    secondary_group_ids: List[int]
    show_dob_date: bool
    show_dob_year: bool
    signature: str
    timezone: str
    use_tfa: bool
    user_group_id: int
    user_state: str
    user_title: str
    visible: bool
    warning_points: int  # Current warning points.
    website: str
    view_url: str
    user_id: int
    username: str
    message_count: int
    question_solution_count: int
    register_date: int
    trophy_points: int
    is_staff: bool
    reaction_score: int
    vote_score: int


class GetUsersParams(BaseModel):
    page: Optional[int] = None


class PostUserParams(BaseModel):
    username: str
    email: str
    password: str
    option: Optional[Dict[str, Any]] = None
    profile: Optional[Dict[str, str]] = None
    privacy: Optional[Dict[str, str]] = None
    visible: Optional[bool] = None
    activity_visible: Optional[bool] = None
    timezone: Optional[str] = None
    custom_title: Optional[str] = None
    user_group_id: Optional[int] = None
    secondary_group_ids: Optional[List[int]] = None
    user_state: Optional[str] = None
    is_staff: Optional[bool] = None
    message_count: Optional[int] = None
    reaction_score: Optional[int] = None
    trophy_points: Optional[int] = None
    username_change_visible: Optional[bool] = None
    dob: Optional[Dict[str, int]] = None
    custom_fields: Optional[Dict[str, str]] = None


class GetUsersFindEmailParams:
    email: str


class GetUsersFindNameParams(BaseModel):
    username: str


class GetUserParams(BaseModel):
    with_posts: Optional[bool] = None
    page: Optional[int] = None


class PostUserUpdateParams(BaseModel):
    option: Optional[Dict[str, Any]] = None
    profile: Optional[Dict[str, str]] = None
    privacy: Optional[Dict[str, str]] = None
    visible: Optional[bool] = None
    activity_visible: Optional[bool] = None
    timezone: Optional[str] = None
    custom_title: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    user_group_id: Optional[int] = None
    secondary_group_ids: Optional[List[int]] = None
    user_state: Optional[str] = None
    is_staff: Optional[bool] = None
    message_count: Optional[int] = None
    reaction_score: Optional[int] = None
    trophy_points: Optional[int] = None
    username_change_visible: Optional[bool] = None
    dob: Optional[Dict[str, int]] = None
    custom_fields: Optional[Dict[str, str]] = None


class DeleteUserParams(BaseModel):
    rename_to: Optional[str] = None


class PostUserAvatarParamsv:
    avatar: BinaryIO  # File upload


class GetUserProfilePostsParams(BaseModel):
    page: Optional[int] = None
