from aiogram import types
from loader import dp, bot
from keyboards.inline.basket_inline_kb import *
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
                "item_id": user[i].item_id,
                "item_price": user[i].item_price
            }
        )

    all_price = 0

    for i in data:
        all_price += i.get('item_price')

    if len(user) == 0:
        await message.answer(f'Корзина пуста.\n\n'
                             f'Перейди в каталог и выбери что-нибудь:)',
                             reply_markup=await go_catalog_kb()
                             )
    else:
        await message.answer(f'У вас в корзине:\n\n'
                             f'Всего товаров - {len(data)} шт.\n\n'
                             f'На сумму - {all_price} руб.',
                             reply_markup=await buy_kb(message.from_user.id)
                             )
    await message.delete()


@dp.callback_query_handler(lambda call: "add_" in call.data)
async def add_product_to_cart(call: types.CallbackQuery):
    await bot.answer_callback_query(callback_query_id=call.id, text='Товар добавлен в корзину.')
    item_id = int(call.data.split('_')[1])
    user_id = call.from_user.id
    item = await get_item(item_id)
    item_price = item.price
    await create_user_basket(user_id=user_id, item_id=item_id, item_price=item_price)


@dp.callback_query_handler(lambda call: "deleteBasket_" in call.data)
async def del_user_cart(call: types.CallbackQuery):
    user_id = int(call.data.split('_')[1])
    await delete_user_basket(user_id)
    await call.message.delete()
    await show_basket(call.message)
