from aiogram import types
from loader import dp, bot


@dp.callback_query_handler(lambda call: "payBasket_" in call.data)
async def pay_user_basket_qiwi(call: types.CallbackQuery):
    user_id = int(call.data.split('_')[1])
    await call.message.answer(f'Ну {call.from_user.full_name} молодец)')
