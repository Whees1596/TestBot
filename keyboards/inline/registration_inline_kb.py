from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def subscribe_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Подписаться!', url='https://t.me/+0jVHYQghr0xhZGMy')
            ],
            [
                InlineKeyboardButton(text='Я подписался!', callback_data='subDone')
            ]
        ]
    )
    return keyboard


async def registration_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Зарегистрироваться!', callback_data='registrDone')
            ]
        ]
    )
    return keyboard

