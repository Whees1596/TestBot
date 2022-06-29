from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def support_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Дмитрий', url='https://t.me/whees'),
                InlineKeyboardButton(text='Анна', url='https://t.me/_______')
            ],
            [
                InlineKeyboardButton(text='Ирина', url='https://t.me/_______'),
                InlineKeyboardButton(text='Николай', url='https://t.me/_______')
            ]
        ]
    )
    return keyboard