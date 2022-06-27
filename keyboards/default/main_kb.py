from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def main_menu() -> ReplyKeyboardMarkup:
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        one_time_keyboard=False,
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text='Каталог'),
                KeyboardButton(text='Поддержка'),
                KeyboardButton(text='История заказов')
            ],
            [
                KeyboardButton(text='Кабинет'),
                KeyboardButton(text='Заказ')
            ]
        ]
    )
    return keyboard