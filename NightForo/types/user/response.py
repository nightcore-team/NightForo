from typing import List, Optional

from pydantic import BaseModel

from ..pagination import Pagination
from ..profile_post import ProfilePost
from . import User


class UsersGetResponse(BaseModel):
    users: List[User]
    pagination: Pagination


class UserCreateResponse(BaseModel):
    success: bool
    user: User


class UserFindEmailResponse(BaseModel):
    user: Optional[User] = None


class UserFindNameResponse(BaseModel):
    exact: Optional[User] = None
    recommendations: List[User]


class UserGetResponse(BaseModel):
    user: User
    profile_posts: Optional[List[ProfilePost]] = None
    pagination: Optional[Pagination] = None


class UserUpdateResponse(BaseModel):
    success: bool
    user: User


class UserDeleteResponse(BaseModel):
    success: bool


class UserAvatarUpdateResponse(BaseModel):
    success: bool


class UserAvatarDeleteResponse(BaseModel):
    success: bool


class UserProfilePostsGetResponse(BaseModel):
    profile_posts: List[ProfilePost]
    pagination: Pagination
