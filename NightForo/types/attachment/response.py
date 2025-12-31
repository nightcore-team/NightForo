from typing import BinaryIO, List, Optional

from pydantic import BaseModel

from .attachment import Attachment

__all__ = (
    "AttachmentDeleteResponse",
    "AttachmentGetDataResponse",
    "AttachmentGetResponse",
    "AttachmentGetThumbnailResponse",
    "AttachmentUploadResponse",
    "AttachmentsCreateNewKeyResponse",
    "AttachmentsGetResponse",
)


class AttachmentsGetResponse(BaseModel):
    attachments: List[Attachment]


class AttachmentUploadResponse(BaseModel):
    attachment: Attachment


class AttachmentsCreateNewKeyResponse(BaseModel):
    key: str
    attachment: Optional[Attachment]


class AttachmentGetResponse(BaseModel):
    attachment: Attachment


class AttachmentDeleteResponse(BaseModel):
    success: bool


class AttachmentGetDataResponse(BaseModel):
    data: BinaryIO


class AttachmentGetThumbnailResponse(BaseModel):
    url: str
