from enum import Enum

__all__ = ("ApiKeyTypeEnum",)


class ApiKeyTypeEnum(Enum):
    USER = "user"
    SUPER_USER = "superuser"
    GUEST = "guest"
