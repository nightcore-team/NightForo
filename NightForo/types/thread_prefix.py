from pydantic import BaseModel


class ThreadPrefix(BaseModel):
    prefix_id: int
    title: str
    description: str
    usage_help: str
    is_usableL: bool  # 	True if the acting user can use (select) this prefix.
    prefix_group_id: int
    display_order: int
    materialized_order: int  # Effective order, taking group ordering into account.
