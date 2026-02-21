from enum import Enum

__all__ = ("ArzGuardGroupsIdsEnum", "ArzGuardGroupsNamesEnum")


class ArzGuardGroupsIdsEnum(Enum):
    FORUM_MANAGERS = 3
    FORUM_ADMINISTRATORS = 25
    FORUM_MODERATORS = 36
    SERVICE_ACCOUNTS = 19
    GAME_ADMINISTRATORS = 17
    SERVER_MANAGERS = 33
    HEAD_MODERATORS = 4
    DEPUTY_HEAD_MODERATORS = 9
    TECH_MODERATORS = 32
    CURATORS_OF_MODERATION = 20
    SENIOR_MODERATORS = 7
    MODERATORS = 8
    BLOCKED_USERS = 5


class ArzGuardGroupsNamesEnum(Enum):
    FORUM_MANAGERS = "(01) Руководители форума"
    FORUM_ADMINISTRATORS = "(02) Администраторы форума"
    FORUM_MODERATORS = "(03) Модераторы форума"
    SERVICE_ACCOUNTS = "(04) Служебные аккаунты"
    GAME_ADMINISTRATORS = "(05) Игровые администраторы"
    SERVER_MANAGERS = "(06) Руководители серверов"
    HEAD_MODERATORS = "(07) Главные модераторы"
    DEPUTY_HEAD_MODERATORS = "(08) Заместители главных модераторов"
    TECH_MODERATORS = "(09) Технические модераторы"
    CURATORS_OF_MODERATION = "(10) Кураторы модерации"
    SENIOR_MODERATORS = "(11) Старшие модераторы"
    MODERATORS = "(12) Модераторы"
    USERS = "(13) Пользователи"
    GUESTS = "(14) Гости"
    BLOCKED_USERS = "(15) Заблокированные пользователи"
