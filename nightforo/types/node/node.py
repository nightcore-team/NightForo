from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from nightforo.types.forum.forum import LinkForumTypeData

from ...types.forum import (
    ForumTypeData,
    SearchForumTypeData,
)
from ...types.node_type import NodeTypeEnum
from ...types.page import PageTypeData

AnyNodeTypeData = Union[
    ForumTypeData,
    SearchForumTypeData,
    PageTypeData,
    LinkForumTypeData,
    Dict[str, Any],
]

__all__ = ("Breadcrumb", "Node")


class Breadcrumb(BaseModel):
    node_id: Optional[int] = None
    title: Optional[str] = None
    node_type_id: Optional[NodeTypeEnum] = None


class Node(BaseModel):
    node_id: int

    title: str
    node_name: Optional[str] = None
    node_type_id: NodeTypeEnum
    breadcrumbs: List[Breadcrumb]
    type_data: Union[
        AnyNodeTypeData,
        Dict[str, Any],
    ]
    view_url: str
    description: str
    parent_node_id: int
    display_order: int
    display_in_list: bool
