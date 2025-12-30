from pydantic import BaseModel

from . import ProfilePostComment


class ProfilePostCommentCreateResponse(BaseModel):
    success: bool
    comment: ProfilePostComment


class ProfilePostCommentGetResponse(BaseModel):
    comment: ProfilePostComment


class ProfilePostCommentUpdateResponse(BaseModel):
    success: bool
    comment: ProfilePostComment


class ProfilePostCommentDeleteResponse(BaseModel):
    success: bool


class ProfilePostCommentReactResponse(BaseModel):
    success: bool
    action: str
