from pydantic import BaseModel

from ..user import User


class MeGetResponse(BaseModel):
    me: User


class MeUpdateResponse(BaseModel):
    success: bool


class MeAvatarUpdateResponse(BaseModel):
    success: bool


class MeAvatarDeleteResponse(BaseModel):
    success: bool


class MeEmailUpdateResponse(BaseModel):
    success: bool
    confirmation_required: bool


class MePasswordUpdateResponse(BaseModel):
    success: bool
