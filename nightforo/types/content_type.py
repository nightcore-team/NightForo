from enum import Enum

__all__ = ("ContentTypeEnum",)


class ContentTypeEnum(Enum):
    POST = "post"
    TROPHY = "trophy"
    USER = "user"
    THREAD = "thread"
    USERNAME_CHANGE = "username_change"
    STR = "str"
    CONTACT = "contact"
    CONVERSATION_MESSAGE = "conversation_message"
