from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def admin_menu() -> ReplyKeyboardMarkup:
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        one_time_keyboard=False,
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text='Добавить товар'),
                KeyboardButton(text='Отмена')
            ],
        ]
    )
    return keyboard