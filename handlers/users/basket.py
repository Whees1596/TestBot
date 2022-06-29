from aiogram import types
from loader import dp
from states import FSMbasket
from aiogram.dispatcher import FSMContext
from utils.db_api.quick_commands import *


@dp.message_handler(text="Заказ")
async def show_basket(message: types.Message):
    await user_basket(message)


async def user_basket(message: types.Message):
    user = await show_user_basket(message.from_user.id)
    data = []
    for i in range(len(user)):
        data.append(
            {
                "item_id": user[i].item_id
            }
        )
    print(data)
    if len(user) == 0:
        await message.answer(f'Корзина пуста.\n\n'
                             f'Перейди в каталог и выбери что-нибудь:)')
    else:
        await message.answer(f'У вас в корзине:\n\n'
                             f'Всего товаров - {len(data)}.\n\n'
                             # f'На сумму - {} руб.'
                             )



@dp.callback_query_handler(lambda call: "add_" in call.data)
async def add_product_to_cart(call: types.CallbackQuery):
    item_id = int(call.data.split('_')[1])
    user_id = call.from_user.id
    await create_user_basket(user_id, item_id)
