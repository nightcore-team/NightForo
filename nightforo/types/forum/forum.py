from typing import Any, Dict, List, Union

from pydantic import BaseModel, field_validator

__all__ = (
    "ForumTypeData",
    "SearchForumTypeData",
)


class ForumTypeData(BaseModel):
    allow_posting: bool
    can_create_thread: bool
    can_upload_attachment: bool
    custom_fields: Dict[str, Any]

    @field_validator("custom_fields", mode="before")
    @classmethod
    def validate_scopes(
        cls, v: Union[Dict[str, Any], List[Any]]
    ) -> Dict[str, Any]:
        if isinstance(v, list):
            v = {}

        return v


class SearchForumTypeData(BaseModel):
    discussion_count: int
    message_count: int


class LinkForumTypeData(BaseModel):
    link_url: str
    redirect_count: int
