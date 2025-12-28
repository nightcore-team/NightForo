from pydantic import BaseModel


class LinkForum(BaseModel):
    link_url: str
    redirect_count: int
