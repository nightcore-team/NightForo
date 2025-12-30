from pydantic import BaseModel

from ..user import User


class AuthTestResponse(BaseModel):
    user: User


class AuthFromSessionResponse(BaseModel):
    success: bool
    user: User


class AuthLoginTokenResponse(BaseModel):
    login_token: str
    login_url: str
    expiry_date: int
