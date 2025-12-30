from typing import List, Optional
from pydantic import BaseModel

from ..post import Post
from . import Thread
from ..pagination import Pagination


class ThreadGetResponse(BaseModel):
    thread: Thread
    first_unread: Optional[Post]
    first_post: Optional[Post]
    last_post: Optional[Post]
    pinned_post: Optional[Post]
    highlighted_posts: Optional[List[Post]]
    posts: List[Post]
    pagination: Pagination


class ThreadCreateResponse(BaseModel):
    success: bool
    thread: Thread
