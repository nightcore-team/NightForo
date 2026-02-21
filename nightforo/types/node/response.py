from typing import Dict, List

from pydantic import BaseModel

from .node import Node

__all__ = (
    "NodeCreateResponse",
    "NodeDeleteResponse",
    "NodeGetResponse",
    "NodeUpdateResponse",
    "NodesFlattenedGetResponse",
    "NodesGetResponse",
)


class NodesGetResponse(BaseModel):
    tree_map: Dict[int, List[int]]
    nodes: List[Node]


class NodeCreateResponse(BaseModel):
    node: Node


class NodesFlat(BaseModel):
    node: Node
    depth: int


class NodesFlattenedGetResponse(BaseModel):
    nodes_flat: List[NodesFlat]


class NodeGetResponse(BaseModel):
    node: Node


class NodeUpdateResponse(BaseModel):
    node: Node


class NodeDeleteResponse(BaseModel):
    success: bool
