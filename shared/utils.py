import os

from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    select_language = State()
    main_menu = State()


TOKEN = os.getenv('translator-token')
REDIS_HOST = os.getenv('redis-host')
REDIS_PASSWORD = os.getenv('redis-password')
SERVER_BASEURL = os.getenv('server-baseurl')
SERVER_SECURE = os.getenv('server-secure')
WEBAPP_BASEURL = os.getenv('webapp-baseurl')


def plural(count: int, words: dict) -> str:
    if int(str(count)[len(str(count))-1]) == 1:
        return words['one']
    elif count > 1:
        return words['many']
