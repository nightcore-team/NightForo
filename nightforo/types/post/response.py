from typing import Optional

from pydantic import BaseModel

from ...types.post_react_state import PostReactStateEnum
from .post import Post

__all__ = (
    "PostCreateResponse",
    "PostDeleteResponse",
    "PostGetResponse",
    "PostMarkSolutionResponse",
    "PostReactResponse",
    "PostUpdateResponse",
    "PostVoteResponse",
)


class PostCreateResponse(BaseModel):
    success: bool
    post: Post


class PostGetResponse(BaseModel):
    post: Post


class PostUpdateResponse(BaseModel):
    success: bool
    post: Post


class PostDeleteResponse(BaseModel):
    success: bool


class PostMarkSolutionResponse(BaseModel):
    success: bool
    new_solution_post: Optional[Post] = None
    old_solution_post: Optional[Post] = None


class PostReactResponse(BaseModel):
    success: bool
    action: PostReactStateEnum


class PostVoteResponse(BaseModel):
    success: bool
    action: PostReactStateEnum
