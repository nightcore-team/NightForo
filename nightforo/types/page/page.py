from pydantic import BaseModel

__all__ = ("PageTypeData",)


class PageTypeData(BaseModel):
    content: str
    publish_date: int
    view_count: int
