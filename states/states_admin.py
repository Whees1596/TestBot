from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMadmin(StatesGroup):
    category_name = State()
    subcategory_name = State()
    category_code = State()
    subcategory_code = State()
    name = State()
    photo = State()
    description = State()
    price = State()
    count = State()