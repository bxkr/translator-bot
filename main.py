import asyncio
import aiogram
from aiogram.filters import Command
import constants

bot = aiogram.Bot(token=constants.TOKEN)
dp = aiogram.Dispatcher()


@dp.message(Command(commands={'start'}))
async def start_handler(message: aiogram.types.Message):
    await message.answer('hello')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
