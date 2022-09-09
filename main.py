import asyncio
import aiogram
import aioredis
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.storage.redis import RedisStorage

from sections import main_menu_router
from shared import TOKEN, UserStates, REDIS_HOST, REDIS_PASSWORD

bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher()


@dp.message(Command(commands={'start'}))
async def start_handler(message: aiogram.types.Message, state: FSMContext):
    if await state.get_state() is None:
        await state.set_state(UserStates.main_menu)
        await message.answer('Привет! Управление осуществляется с помощью кнопок под клавиатурой или сообщением')


async def main():
    dp.fsm.storage = RedisStorage(aioredis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD))
    dp.include_router(main_menu_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
