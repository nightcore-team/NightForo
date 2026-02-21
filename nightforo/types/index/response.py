from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, field_validator

from ...types.api_key_type import ApiKeyTypeEnum
from ...types.api_scopes import APIScopeIdsEnum

__all__ = ("ApiKey", "IndexGetResponse")


class ApiKey(BaseModel):
    type: ApiKeyTypeEnum
    user_id: Optional[int] = None
    allow_all_scopes: bool
    scopes: Dict[APIScopeIdsEnum, bool]

    @field_validator("scopes", mode="before")
    @classmethod
    def validate_scopes(
        cls, v: Union[Dict[APIScopeIdsEnum, bool], List[Any]]
    ) -> Dict[APIScopeIdsEnum, bool]:
        if isinstance(v, list):
            v = {}

        return v


class IndexGetResponse(BaseModel):
    version_id: int
    site_title: str
    base_url: str
    api_url: str
    key: ApiKey
