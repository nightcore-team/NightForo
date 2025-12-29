from typing import Dict, List, Optional
from pydantic import BaseModel
from .user import User


class Conversation(BaseModel):
    username: str  # Name of the user that started the conversation
    recipients: Dict[str, str]  # Key-value pair of recipient user IDs and names
    is_starred: bool  # True if the viewing user starred the conversation
    is_unread: Optional[
        bool
    ]  # If accessing as a user, true if this conversation is unread
    can_edit: bool
    can_reply: bool
    can_invite: bool
    can_upload_attachment: bool
    view_url: str
    conversation_id: int
    title: str
    user_id: int
    start_date: int
    open_invite: bool
    conversation_open: bool
    reply_count: int
    recipient_count: int
    first_message_id: int
    last_message_date: int
    last_message_id: int
    last_message_user_id: int
    Starter: User


class GetConversationsParams(BaseModel):
    page: Optional[int] = None
    starter_id: Optional[int] = None
    receiver_id: Optional[int] = None
    starred: Optional[bool] = None
    unread: Optional[bool] = None


class PostConversationParams(BaseModel):
    recipient_ids: List[int]
    title: str
    message: str
    attachment_key: Optional[str] = None
    conversation_open: Optional[bool] = None
    open_invite: Optional[bool] = None


class GetConversationParams(BaseModel):
    with_messages: Optional[bool] = None
    page: Optional[int] = None


class PostConversationUpdateParams(BaseModel):
    title: Optional[str] = None
    open_invite: Optional[bool] = None
    conversation_open: Optional[bool] = None


class DeleteConversationParams(BaseModel):
    ignore: Optional[bool] = None


class PostConversationInviteParams(BaseModel):
    recipient_ids: List[int]


class PostConversationMarkReadParams(BaseModel):
    date: Optional[int] = None


class GetConversationMessagesParams(BaseModel):
    page: Optional[int] = None


class PostConversationStarParams(BaseModel):
    star: Optional[bool] = None
