from typing import List, Optional

from pydantic import BaseModel, field_serializer

__all__ = (
    "ConversationCreateParams",
    "ConversationDeleteParams",
    "ConversationGetMessagesParams",
    "ConversationGetParams",
    "ConversationInviteParams",
    "ConversationMarkReadParams",
    "ConversationStarParams",
    "ConversationUpdateParams",
    "ConversationsGetParams",
)


class ConversationsGetParams(BaseModel):
    page: Optional[int] = None
    starter_id: Optional[int] = None
    receiver_id: Optional[int] = None
    starred: Optional[bool] = None
    unread: Optional[bool] = None

    @field_serializer("starred", "unread")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ConversationCreateParams(BaseModel):
    recipient_ids: List[int]
    title: str
    message: str
    attachment_key: Optional[str] = None
    conversation_open: Optional[bool] = None
    open_invite: Optional[bool] = None

    @field_serializer("open_invite", "conversation_open")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ConversationGetParams(BaseModel):
    with_messages: Optional[bool] = None
    page: Optional[int] = None

    @field_serializer("with_messages")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ConversationUpdateParams(BaseModel):
    title: Optional[str] = None
    open_invite: Optional[bool] = None
    conversation_open: Optional[bool] = None

    @field_serializer("open_invite", "conversation_open")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ConversationDeleteParams(BaseModel):
    ignore: bool

    @field_serializer("ignore")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class ConversationInviteParams(BaseModel):
    recipient_ids: List[int]


class ConversationMarkReadParams(BaseModel):
    date: int


class ConversationGetMessagesParams(BaseModel):
    page: int


class ConversationStarParams(BaseModel):
    star: bool

    @field_serializer("star")
    def serialize_bool(self, v: bool):
        return 1 if v else 0
