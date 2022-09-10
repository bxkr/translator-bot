import json

from aiogram import Router, types, F
import aiohttp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from shared import UserStates, main_menu_keyboard, SERVER_SECURE, SERVER_BASEURL, plural, translations, \
    WEBAPP_BASEURL, PluralCases

main_menu_router = Router()


def webapp_keyboard(available: list[str]) -> InlineKeyboardMarkup:
    json_format = json.dumps(available).replace('"', '%22')
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f'🔤 Выбрать из {len(available)} {plural(len(available), translations, PluralCases.GENITIVE)}',
                web_app=WebAppInfo(url=f'{WEBAPP_BASEURL}?available={json_format}'))
        ],
        [
            InlineKeyboardButton(text=f'🔄 Обновить', callback_data='update-translations')
        ]
    ])


async def answer_webapp(message: types.Message):
    async with aiohttp.ClientSession().get(f'{SERVER_BASEURL}get_list?{SERVER_SECURE}') as request:
        available = [str(i[1]).capitalize() for i in (await request.json())]
        await message.edit_text(
            f'На данный момент существует {len(available)} '
            f'{plural(len(available), translations, PluralCases.NOMINATIVE)}. Вы можете выбрать и '
            f'посмотреть один из них с помощью кнопки внизу. Чтобы обновить список, нажмите '
            f'"Обновить".', reply_markup=webapp_keyboard(available))


@main_menu_router.message(UserStates.main_menu, F.web_app_data)
async def got_data(message: types.Message):
    await message.answer(f'Твоё слово: {message.web_app_data.data}\nПеревод: Привет')


@main_menu_router.message(UserStates.main_menu, F.text == 'Существующие переводы')
async def send_webapp(message: types.Message):
    loading = await message.answer('Получаю данные...')
    await answer_webapp(loading)


@main_menu_router.callback_query(UserStates.main_menu, F.data == 'update-translations')
async def update_translations(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Обновляю данные...')
    await answer_webapp(callback_query.message)
    await callback_query.answer('Обновлено!')


@main_menu_router.message(UserStates.main_menu)
async def inline_result(message: types.Message):
    async with aiohttp.ClientSession().get(f'{SERVER_BASEURL}get_list?{SERVER_SECURE}') as request:
        for record in await request.json():
            if (record[1] == message.text) or (record[1] == message.text.lower()) or (
                    record[1] == message.text.capitalize()):
                await message.answer(f'Перевод {message.text} - {record[2]}')
                return
        await message.answer('Мы пока не перевели это слово :(')


@main_menu_router.message(UserStates.main_menu)
async def echo_main(message: types.Message):
    await message.answer('Ты в главном меню!', reply_markup=main_menu_keyboard)
