from typing import Literal, Optional, TypeVar, Union

from pydantic import BaseModel, field_serializer

from ...types.forum.forum import (
    ForumTypeData,
    LinkForumTypeData,
    SearchForumTypeData,
)
from ...types.node.node import AnyNodeTypeData
from ...types.node_type import NodeTypeEnum
from ...types.page.page import PageTypeData

__all__ = (
    "AnyNodeCreateParams",
    "CategoryNodeCreateParams",
    "ForumNodeCreateParams",
    "LinkForumNodeCreateParams",
    "NodeDeleteParams",
    "NodeUpdateParams",
    "PageNodeCreateParams",
    "SearchForumNodeCreateParams",
)


T = TypeVar("T")


class NodeDeleteParams(BaseModel):
    delete_children: Optional[bool] = None

    @field_serializer("delete_children")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class NodeCreateData(BaseModel):
    title: str
    node_name: Optional[str] = None
    description: Optional[str] = None
    parent_node_id: int = 0
    display_order: Optional[int] = None
    display_in_list: Optional[bool] = None

    @field_serializer("display_in_list")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class _NodeCreateParams(BaseModel):
    node: NodeCreateData


class CategoryNodeCreateParams(_NodeCreateParams):
    node_type_id: Literal[NodeTypeEnum.CATEGORY] = NodeTypeEnum.CATEGORY

    @field_serializer("node_type_id")
    def serialize_type(self, v: NodeTypeEnum):
        return v.value


class SearchForumNodeCreateParams(_NodeCreateParams):
    node_type_id: Literal[NodeTypeEnum.SEARCH_FORUM] = (
        NodeTypeEnum.SEARCH_FORUM
    )
    type_data: Optional[SearchForumTypeData] = None

    @field_serializer("node_type_id")
    def serialize_type(self, v: NodeTypeEnum):
        return v.value


class PageNodeCreateParams(_NodeCreateParams):
    node_type_id: Literal[NodeTypeEnum.PAGE]
    type_data: Optional[PageTypeData] = None

    @field_serializer("node_type_id")
    def serialize_type(self, v: NodeTypeEnum):
        return v.value


class LinkForumNodeCreateParams(_NodeCreateParams):
    node_type_id: Literal[NodeTypeEnum.LINK_FORUM] = NodeTypeEnum.LINK_FORUM
    type_data: Optional[LinkForumTypeData] = None

    @field_serializer("node_type_id")
    def serialize_type(self, v: NodeTypeEnum):
        return v.value


class ForumNodeCreateParams(_NodeCreateParams):
    node_type_id: Literal[NodeTypeEnum.FORUM] = NodeTypeEnum.FORUM
    type_data: Optional[ForumTypeData] = None

    @field_serializer("node_type_id")
    def serialize_type(self, v: NodeTypeEnum):
        return v.value


class NodeUpdateData(BaseModel):
    title: Optional[str] = None
    node_name: Optional[str] = None
    description: Optional[str] = None
    parent_node_id: Optional[int] = None
    display_order: Optional[int] = None
    display_in_list: Optional[bool] = None

    @field_serializer("display_in_list")
    def serialize_bool(self, v: bool):
        return 1 if v else 0


class NodeUpdateParams(BaseModel):
    node: NodeUpdateData
    type_data: Optional[AnyNodeTypeData] = None


AnyNodeCreateParams = Union[
    ForumNodeCreateParams,
    SearchForumNodeCreateParams,
    CategoryNodeCreateParams,
    PageNodeCreateParams,
    LinkForumNodeCreateParams,
]
