from enum import Enum

__all__ = ("ArzGuardGroupsIdsEnum", "ArzGuardGroupsNamesEnum")


class ArzGuardGroupsIdsEnum(Enum):
    FORUM_MANAGERS = 3
    FORUM_ADMINISTRATORS = 25
    FORUM_MODERATORS = 36
    SERVICE_ACCOUNTS = 19
    REPRESENTATIVE_ARIZONA_GAMES = 38
    GAME_ADMINISTRATORS = 17
    SERVER_MANAGERS = 33
    HEAD_MODERATORS = 4
    DEPUTY_HEAD_MODERATORS = 9
    TECH_MODERATORS = 32
    CURATORS_OF_MODERATION = 20
    SENIOR_MODERATORS = 7
    MODERATORS = 8
    BLOCKED_USERS = 5
    USERS = 2


class ArzGuardGroupsNamesEnum(Enum):
    FORUM_MANAGERS = "(01) Руководители форума"
    FORUM_ADMINISTRATORS = "(02) Администраторы форума"
    FORUM_MODERATORS = "(03) Модераторы форума"
    SERVICE_ACCOUNTS = "(04) Служебные аккаунты"
    REPRESENTATIVE_ARIZONA_GAMES = "(05) Представители Arizona Games"
    GAME_ADMINISTRATORS = "(06) Игровые администраторы"
    SERVER_MANAGERS = "(07) Руководители серверов"
    TECH_MODERATORS = "(08) Технические модераторы"
    HEAD_MODERATORS = "(09) Главные модераторы"
    DEPUTY_HEAD_MODERATORS = "(10) Заместители главных модераторов"
    CURATORS_OF_MODERATION = "(11) Кураторы модерации"
    SENIOR_MODERATORS = "(12) Старшие модераторы"
    MODERATORS = "(13) Модераторы"
    USERS = "(14) Пользователи"
    GUESTS = "(15) Гости"
    BLOCKED_USERS = "(16) Заблокированные пользователи"
