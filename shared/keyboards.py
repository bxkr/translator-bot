from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Существующие переводы', web_app=WebAppInfo(url=
                                                                        'https://translator-bot-front.herokuapp.com/'))
    ]
])
