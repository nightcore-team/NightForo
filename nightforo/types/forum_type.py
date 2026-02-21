from enum import Enum

__all__ = ("ForumTypeEnum",)


class ForumTypeEnum(Enum):
    DISCUSSION = "discussion"
    QUESTION = "question"
    SUGGESTION = "suggestion"
