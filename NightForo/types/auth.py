from typing import Optional

from pydantic import BaseModel


class PostAuthParams(BaseModel):
    login: str
    password: str
    limit_ip: Optional[str] = None


class PostAuthFromSessionParams(BaseModel):
    session_id: Optional[str] = None
    remember_cookie: Optional[str] = None


class PostAuthLoginTokenParams(BaseModel):
    user_id: int
    limit_ip: Optional[str] = None
    return_url: Optional[str] = None
    force: Optional[bool] = None
    remember: Optional[bool] = None
