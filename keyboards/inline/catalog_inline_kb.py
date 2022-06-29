from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.quick_commands import get_categories, count_items, get_subcategories, get_items

menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id)


async def categories_kb():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)

    categories = await get_categories()
    for category in categories:
        number_of_items = await count_items(category.category_code)
        button_text = f'{category.category_name} ({number_of_items} шт.)'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category.category_code
                                           )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


async def subcategories_kb(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=2)

    subcategories = await get_subcategories(category)
    for subcategory in subcategories:
        number_of_items = await count_items(category_code=category, subcategory_code=subcategory.subcategory_code)
        button_text = f'{subcategory.subcategory_name} ({number_of_items} шт.)'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           subcategory=subcategory.subcategory_code
                                           )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=CURRENT_LEVEL - 1))
    )

    return markup


async def items_kb(category, subcategory):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    items = await get_items(category, subcategory)
    for item in items:
        button_text = f'{item.name} - ({item.price} руб.)'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           subcategory=subcategory,
                                           item_id=item.id_item
                                           )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                                                            category=category))
    )
    return markup


def item_kb(category, subcategory, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text='В корзину', callback_data=f'add_{item_id}')
    )
    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                             category=category, subcategory=subcategory))
    )

    return markup

