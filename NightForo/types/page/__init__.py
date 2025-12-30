from pydantic import BaseModel


class Page(BaseModel):
    publish_date: int
    view_count: int
