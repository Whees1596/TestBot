from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def go_catalog_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='В каталог', callback_data='gotocatalog')
            ]
        ]
    )
    return keyboard


async def buy_kb(user_id) -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Оплатить', callback_data=f'checkBasket_{user_id}'),
            ],
            [
                InlineKeyboardButton(text='Очистить', callback_data=f'deleteBasket_{user_id}')
            ]
        ]
    )
    return keyboard