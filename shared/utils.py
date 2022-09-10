import os

from aiogram.fsm.state import StatesGroup, State
from enum import Enum

TOKEN = os.getenv('translator-token')
REDIS_HOST = os.getenv('redis-host')
REDIS_PASSWORD = os.getenv('redis-password')
SERVER_BASEURL = os.getenv('server-baseurl')
SERVER_SECURE = os.getenv('server-secure')
WEBAPP_BASEURL = os.getenv('webapp-baseurl')


class PluralCases(Enum):
    NOMINATIVE = 0  # Именительный
    GENITIVE = 1  # Родительный
    ACCUSATIVE = 2  # Винительный
    DATIVE = 3  # Дательный
    INSTRUMENTAL = 4  # Творительный
    PREPOSITIONAL = 5  # Предложный


class UserStates(StatesGroup):
    select_language = State()
    main_menu = State()


def plural(count: int, words: dict, case: PluralCases) -> str:
    if case == PluralCases.NOMINATIVE or \
            case == PluralCases.GENITIVE or \
            case == PluralCases.ACCUSATIVE or \
            case == PluralCases.DATIVE or \
            case == PluralCases.INSTRUMENTAL or \
            case == PluralCases.PREPOSITIONAL:
        if (int(str(count)[len(str(count)) - 1]) == 1 and len(str(count)) < 10) or (
                len(str(count)) >= 10 and int(str(count)[len(str(count)) - 1]) == 1 and int(
                str(count)[len(str(count)) - 1] + str(count)[len(str(count)) - 2]) != 11):
            return words[case]['one']
        if case == PluralCases.NOMINATIVE or case == PluralCases.ACCUSATIVE:
            if (int(str(count)[len(str(count)) - 1]) in [2, 3, 4] and len(str(count)) < 10) or (
                    len(str(count)) >= 10 and int(str(count)[len(str(count)) - 1]) in [2, 3, 4] and int(
                    str(count)[len(str(count)) - 1] + str(count)[len(str(count)) - 2]) not in [12, 13, 14]):
                return words[case]['few']
            return words[case]['many']
        if case == PluralCases.GENITIVE or \
                case == PluralCases.DATIVE or \
                case == PluralCases.INSTRUMENTAL or \
                case == PluralCases.PREPOSITIONAL:
            return words[case]['many']
