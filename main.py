import asyncio
import aiogram
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from utils import *

bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher()


@dp.message(Command(commands={'start'}))
async def start_handler(message: aiogram.types.Message, state: FSMContext):
    if await state.get_state() is None:
        await state.set_state(UserStates.main_menu)
        await message.answer('Hello!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
