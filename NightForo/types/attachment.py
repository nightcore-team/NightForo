from typing import BinaryIO, List, Optional
from pydantic import BaseModel


class Attachment(BaseModel):
    filename: str
    file_size: int
    height: int
    width: int
    thumbnail_url: str
    direct_url: str
    is_video: bool
    is_audio: bool
    attachment_id: int
    content_type: str
    content_id: int
    attach_date: int
    view_count: int


class GetAttachmentsParams(BaseModel):
    key: str


class PostAttachmentParams(BaseModel):
    key: str
    attachment: BinaryIO  # File upload


class PostAttachmentsNewKeyParams(BaseModel):
    type: str
    context: Optional[List[str]] = None
    attachment: Optional[BinaryIO] = None  # File upload
