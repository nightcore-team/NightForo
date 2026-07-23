from enum import Enum

__all__ = ("ArzGuardGroupsIdsEnum", "ArzGuardGroupsNamesEnum")


class ArzGuardGroupsIdsEnum(Enum):
    SERVICE_ACCOUNTS = 19
    PROJECT_MANAGERS = 3
    PROJECT_DEVELOPERS = 39
    FORUM_ADMINISTRATORS = 25
    FORUM_MODERATORS = 36
    ARIZONA_GAMES_REPRESENTATIVES = 38
    GAME_ADMINISTRATORS = 17
    SERVER_MANAGERS = 33
    DEPUTY_SERVER_MANAGERS = 40
    TECHNICAL_ADMINISTRATORS = 32
    HEAD_MODERATORS = 4
    DEPUTY_HEAD_MODERATORS = 9
    TECHNICAL_MODERATORS = 41
    MODERATION_CURATORS = 20
    SENIOR_MODERATORS = 7
    MODERATORS = 8
    USERS = 2
    GUESTS = 1
    BLOCKED_USERS = 5


class ArzGuardGroupsNamesEnum(Enum):
    SERVICE_ACCOUNTS = "(*) Служебные аккаунты"
    PROJECT_MANAGERS = "(01) Руководители проекта"
    PROJECT_DEVELOPERS = "(02) Разработчики проекта"
    FORUM_ADMINISTRATORS = "(03) Администраторы форума"
    FORUM_MODERATORS = "(04) Модераторы форума"
    ARIZONA_GAMES_REPRESENTATIVES = "(05) Представители Arizona Games"
    GAME_ADMINISTRATORS = "(06) Игровые администраторы"
    SERVER_MANAGERS = "(07) Руководители серверов"
    DEPUTY_SERVER_MANAGERS = "(08) Заместители руководителей серверов"
    TECHNICAL_ADMINISTRATORS = "(09) Технические администраторы"
    HEAD_MODERATORS = "(10) Главные модераторы"
    DEPUTY_HEAD_MODERATORS = "(11) Заместители главных модераторов"
    TECHNICAL_MODERATORS = "(12) Технические модераторы"
    MODERATION_CURATORS = "(13) Кураторы модерации"
    SENIOR_MODERATORS = "(14) Старшие модераторы"
    MODERATORS = "(15) Модераторы"
    USERS = "(16) Пользователи"
    GUESTS = "(17) Гости"
    BLOCKED_USERS = "(18) Заблокированные пользователи"
