from enum import Enum

__all__ = ("NodeTypeEnum",)


class NodeTypeEnum(Enum):
    CATEGORY = "Category"
    FORUM = "Forum"
    PAGE = "Page"
    LINK_FORUM = "LinkForum"
    SEARCH_FORUM = "SearchForum"
