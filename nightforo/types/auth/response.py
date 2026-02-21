from typing import Optional

from pydantic import BaseModel

from ..user import User

__all__ = (
    "AuthFromSessionResponse",
    "AuthLoginTokenResponse",
    "AuthTestResponse",
)


class AuthTestResponse(BaseModel):
    user: User


class AuthFromSessionResponse(BaseModel):
    success: bool
    user: Optional[User] = None


class AuthLoginTokenResponse(BaseModel):
    login_token: str
    login_url: str
    expiry_date: int
