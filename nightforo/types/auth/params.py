from typing import Optional

from pydantic import BaseModel, field_serializer

__all__ = ("AuthFromSessionParams", "AuthLoginTokenParams", "AuthTestParams")


class AuthFromSessionParams(BaseModel):
    session_id: Optional[str] = None
    remember_cookie: Optional[str] = None


class AuthLoginTokenParams(BaseModel):
    user_id: int
    limit_ip: Optional[str] = None
    return_url: Optional[str] = None
    force: Optional[bool] = None
    remember: Optional[bool] = None

    @field_serializer("force", "remember")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class AuthTestParams(BaseModel):
    login: str
    password: str
    limit_ip: Optional[str] = None
