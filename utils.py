import os

from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    select_language = State()
    main_menu = State()


TOKEN = os.getenv('translator-token')
