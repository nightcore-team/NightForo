from pydantic import BaseModel


class Pagination(BaseModel):
    current_page: int
    last_page: int
    per_page: int
    shown: int
    total: int
