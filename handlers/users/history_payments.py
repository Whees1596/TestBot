from aiogram import types
from loader import dp, bot
from utils.db_api.quick_commands import *
from keyboards.inline.basket_inline_kb import *


@dp.message_handler(text="История заказов")
async def user_profile(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    payments = await get_all_history_payment_user(message.from_user.id)
    data = []
    if len(payments) == 0:
        await bot.send_message(message.chat.id,
                               f'Пока заказов нет :(\n\n'
                               f'Исправь это!',
                               reply_markup=await go_catalog_kb())
    else:
        for i in range(len(payments)):
            if payments[i].status == 'paid':
                data.append(
                    {
                        "id_payments": payments[i].id,
                        "items_id": payments[i].items_id,
                        "amount": payments[i].amount,
                        "bonus": payments[i].bonus,
                        "create_pay": payments[i].updated_at,
                        "status": payments[i].status
                    }
                )
        await bot.send_message(message.chat.id,
                               f'Ваша история заказов:')
        for i in data:
            await bot.send_message(message.chat.id,
                                   f'Заказ #{i.get("id_payments")}:\n\n'
                                   f'       id товара(через запятую): {i.get("items_id")}\n'
                                   f'       На сумму: {i.get("amount")} руб.\n'
                                   f'       Начисленно бонусов: {i.get("bonus")}\n'
                                   f'       Дата заказа: {i.get("create_pay")}\n\n'
                                   f'Статус заказа:\n'
                                   f'       {i.get("status")}'
                                   )
