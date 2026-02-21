from enum import Enum

__all__ = ("ThreadTypeEnum",)


class ThreadTypeEnum(Enum):
    DISCUSSION = "discussion"
    REDIRECT = "redirect"
    QUESTION = "question"
    POLL = "poll"
    SUGGESTION = "suggestion"
    ARTICLE = "article"
