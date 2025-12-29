from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class Breadcrumb(BaseModel):
    node_id: int
    title: str
    node_type_id: str


class Node(BaseModel):
    breadcrumbs: List[
        Breadcrumb
    ]  # A list of breadcrumbs for this node, including the node_id, title, and node_type_id
    type_data: Dict[
        str, Any
    ]  # Data related to the specific node type this represents. Contents will vary significantly.
    view_url: str
    node_id: int
    title: str
    node_name: str
    description: str
    node_type_id: str
    parent_node_id: int
    display_order: int
    display_in_list: bool


class PostNodeParams(BaseModel):
    node: Dict[str, Any]
    type_data: Dict[str, Any]
    node_type_id: str


class PostNodeUpdateParams(BaseModel):
    node: Dict[str, Any]
    type_data: Dict[str, Any]


class DeleteNodeParams(BaseModel):
    delete_children: Optional[bool] = None
