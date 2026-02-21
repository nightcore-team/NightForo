from typing import Dict, List, Optional

from pydantic import BaseModel, field_serializer

from ..groups import ArzGuardGroupsIdsEnum
from .user import DateOfBirth, Option, Privacy, Profile

__all__ = (
    "UserCreateParams",
    "UserDeleteParams",
    "UserDemoteParams",
    "UserGetParams",
    "UserProfilePostsGetParams",
    "UserPromoteParams",
    "UserUpdateParams",
    "UsersFindEmailParams",
    "UsersFindNameParams",
    "UsersGetParams",
)


class UsersGetParams(BaseModel):
    page: Optional[int] = None


class UserCreateParams(BaseModel):
    username: str
    email: str
    password: str
    option: Optional[Option] = None
    profile: Optional[Profile] = None
    privacy: Optional[Privacy] = None
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
    custom_fields: Optional[str] = None

    @field_serializer(
        "visible", "activity_visible", "is_staff", "username_change_visible"
    )
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class UsersFindEmailParams(BaseModel):
    email: str


class UsersFindNameParams(BaseModel):
    username: str


class UserGetParams(BaseModel):
    with_posts: Optional[bool] = None
    page: Optional[int] = None

    @field_serializer("with_posts")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class UserUpdateParams(BaseModel):
    option: Optional[Option] = None
    profile: Optional[Profile] = None
    privacy: Optional[Privacy] = None
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
    dob: Optional[DateOfBirth] = None
    custom_fields: Optional[str] = None

    @field_serializer(
        "visible", "activity_visible", "is_staff", "username_change_visible"
    )
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class UserDeleteParams(BaseModel):
    rename_to: str


class UserProfilePostsGetParams(BaseModel):
    page: int


class UserDemoteParams(BaseModel):
    group: ArzGuardGroupsIdsEnum

    @field_serializer("group")
    def serialize_group(self, v: ArzGuardGroupsIdsEnum):
        return v.value


class UserPromoteParams(BaseModel):
    group: ArzGuardGroupsIdsEnum

    @field_serializer("group")
    def serialize_group(self, v: ArzGuardGroupsIdsEnum):
        return v.value
