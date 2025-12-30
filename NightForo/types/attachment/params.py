from typing import BinaryIO, List, Optional

from pydantic import BaseModel


class AttachmentsGetParams(BaseModel):
    key: str


class AttachmentUploadParams(BaseModel):
    key: str
    attachment: BinaryIO


class AttachmentsCreateNewKeyParams(BaseModel):
    type: str
    context: Optional[List[str]] = None
    attachment: Optional[BinaryIO] = None
