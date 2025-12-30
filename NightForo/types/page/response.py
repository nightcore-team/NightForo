from typing import List, Optional
from pydantic import BaseModel


class ApiKey(BaseModel):
    type: str
    user_id: Optional[int] = None
    allow_all_scopes: bool
    scopes: List[str]


class IndexGetResponse(BaseModel):
    version_id: int
    site_title: str
    base_url: str
    api_url: str
    key: ApiKey
