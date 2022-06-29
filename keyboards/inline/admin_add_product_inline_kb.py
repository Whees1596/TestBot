from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def select_category_admin_inline_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Одежда', callback_data='clothes'),
                InlineKeyboardButton(text='Обувь', callback_data='shoes')
            ],
            [
                InlineKeyboardButton(text='Аксессуары', callback_data='accessories'),
                InlineKeyboardButton(text='Сумки', callback_data='bags'),
            ],
        ]
    )
    return keyboard


async def select_sub_category_clothes_admin_inline_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Джинсы и брюки', callback_data='jeans_and_trousers'),
                InlineKeyboardButton(text='Толстовки и свитеры', callback_data='hoodies_and_sweaters'),
                InlineKeyboardButton(text='Футболки', callback_data='t-shirts'),

            ],
            [
                InlineKeyboardButton(text='Верхняя одежда', callback_data='outerwear'),
                InlineKeyboardButton(text='Шорты', callback_data='shorts'),
                InlineKeyboardButton(text='Спортивная', callback_data='sports')
            ],
        ]
    )
    return keyboard


async def select_sub_category_shoes_admin_inline_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Кроссовки', callback_data='sneakers'),
                InlineKeyboardButton(text='Кеды', callback_data='low_sneakers'),
                InlineKeyboardButton(text='Шлепанцы', callback_data='flip-flops')

            ],
            [
                InlineKeyboardButton(text='Туфли', callback_data='off_shoes'),
                InlineKeyboardButton(text='Ботинки', callback_data='boots')
            ],
        ]
    )
    return keyboard


async def select_sub_category_bags_admin_inline_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Рюкзаки', callback_data='backpacks'),
                InlineKeyboardButton(text='Сумки', callback_data='sub_bags'),
                InlineKeyboardButton(text='"Бананки"', callback_data='"bananas"')

            ],
        ]
    )
    return keyboard


async def select_sub_category_accessories_admin_inline_kb() -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Часы', callback_data='watch'),
                InlineKeyboardButton(text='Ремни', callback_data='belts'),
                InlineKeyboardButton(text='Очки', callback_data='glasses')

            ],
        ]
    )
    return keyboard
