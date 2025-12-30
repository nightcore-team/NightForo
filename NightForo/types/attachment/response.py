from typing import BinaryIO, List, Optional
from pydantic import BaseModel

from . import Attachment


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


class AttachmentGetData(BaseModel):
    data: BinaryIO


class AttachmentGetThumbnail(BaseModel):
    url: str
