from typing import List, Optional

from pydantic import BaseModel

from ..conversation import Conversation
from ..attachment import Attachment
from ..user import User


class ConversationMessage(BaseModel):
    username: str
    is_unread: (
        Optional[
            bool
        ]  #  If accessing as a user, true if this conversation message is unread
    )
    message_parsed: str  # HTML parsed version of the message contents.
    can_edit: bool
    can_react: bool
    view_url: str
    Conversation: Conversation  # If requested by context, the conversation this message is part of.
    Attachments: Optional[
        List[Attachment]
    ]  # If there are attachments to this message, a list of attachments.
    is_reacted_to: bool  # True if the viewing user has reacted to this content
    visitor_reaction_id: Optional[
        int
    ]  # If the viewer reacted, the ID of the reaction they used
    message_id: int
    conversation_id: int
    message_date: int
    user_id: int
    message: str
    attach_count: int
    reaction_score: int
    User: User
