from typing import Optional
from pydantic import BaseModel


class Forum(BaseModel):
    forum_type_id: str
    allow_posting: bool
    require_prefix: bool
    min_tags: int


class GetForumParams(BaseModel):
    with_threads: Optional[bool] = None
    page: Optional[int] = None
    prefix_id: Optional[int] = None
    starter_id: Optional[int] = None
    last_days: Optional[int] = None
    unread: Optional[bool] = None
    thread_type: Optional[str] = None
    order: Optional[str] = None
    direction: Optional[str] = None


class PostForumMarkReadParams(BaseModel):
    date: Optional[int] = None


class GetForumThreadsParams(BaseModel):
    page: Optional[int] = None
    prefix_id: Optional[int] = None
    starter_id: Optional[int] = None
    last_days: Optional[int] = None
    unread: Optional[bool] = None
    thread_type: Optional[str] = None
    order: Optional[str] = None
    direction: Optional[str] = None
