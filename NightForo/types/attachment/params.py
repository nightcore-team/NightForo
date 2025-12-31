from typing import BinaryIO, List, Optional

from pydantic import BaseModel, ConfigDict

__all__ = (
    "AttachmentUploadParams",
    "AttachmentsCreateNewKeyParams",
    "AttachmentsGetParams",
)


class AttachmentsGetParams(BaseModel):
    key: str


class AttachmentUploadParams(BaseModel):
    key: str
    attachment: BinaryIO

    model_config = ConfigDict(arbitrary_types_allowed=True)


class AttachmentsCreateNewKeyParams(BaseModel):
    type: str
    context: Optional[List[str]] = None
    attachment: Optional[BinaryIO] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
