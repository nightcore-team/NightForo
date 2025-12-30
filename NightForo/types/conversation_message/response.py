from pydantic import BaseModel

from . import ConversationMessage


class ConversationMessageReplyResponse(BaseModel):
    success: bool
    message: ConversationMessage


class ConversationMessageUpdateResponse(BaseModel):
    success: bool
    message: ConversationMessage


class ConversationMessageReactResponse(BaseModel):
    success: bool
    action: str


class ConversationMessageGetResponse(BaseModel):
    message: ConversationMessage
