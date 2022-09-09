from aiogram import Router, types
from shared import UserStates, main_menu_keyboard

main_menu_router = Router()


@main_menu_router.message(UserStates.main_menu)
async def echo_main(message: types.Message):
    await message.answer('Ты в главном меню!', reply_markup=main_menu_keyboard)
