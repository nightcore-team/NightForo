from typing import Any, Dict, Optional

from pydantic import BaseModel, field_serializer

from nightforo.types.content_type import ContentTypeEnum

__all__ = (
    "AttachmentUploadParams",
    "AttachmentsCreateNewKeyParams",
    "AttachmentsGetParams",
)


class AttachmentsGetParams(BaseModel):
    key: str


class AttachmentUploadParams(BaseModel):
    key: str


class AttachmentsCreateNewKeyParams(BaseModel):
    type: ContentTypeEnum
    context: Optional[Dict[str, Any]] = None

    @field_serializer("type")
    def serialize_type(self, v: ContentTypeEnum):
        return v.value
