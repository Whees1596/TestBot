from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMbasket(StatesGroup):
    item_id = State()
    user_id = State()