from typing import Dict, Optional

from pydantic import BaseModel

from ..user import User

__all__ = ("Conversation",)


class Conversation(BaseModel):
    username: str  # Name of the user that started the conversation
    recipients: Dict[
        str, str
    ]  # Key-value pair of recipient user IDs and names
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
