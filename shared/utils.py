import os

from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    select_language = State()
    main_menu = State()


TOKEN = os.getenv('translator-token')
REDIS_HOST = os.getenv('redis-host')
REDIS_PASSWORD = os.getenv('redis-password')
