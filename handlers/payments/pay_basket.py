from aiogram import types
from loader import dp, bot
from utils.db_api.quick_commands import *
from keyboards.inline.pay_inline_kb import *
from keyboards.default.main_kb import *
from data.config import admins


@dp.callback_query_handler(lambda call: "checkBasket_" in call.data)
async def check_user_basket(call: types.CallbackQuery):
    user_id = int(call.data.split('_')[1])
    user_basket = await show_user_basket(user_id)
    data = []
    for i in range(len(user_basket)):
        data.append(
            {
                "item_id": user_basket[i].item_id,
                "item_price": user_basket[i].item_price
            }
        )

    amount = 0
    items_id_list = []

    for i in data:
        amount += i.get('item_price')
        items_id_list.append(
            {
                'item_id': i.get('item_id')
            }
        )

    items_id = ''

    for i in items_id_list:
        items_id += str(i.get('item_id')) + ','

    items_id = items_id[:-1]
    status = 'not paid'
    bonus = amount * 0.1
    unique_id = str(str(user_id)+str(amount)+str(bonus)+str(items_id))

    await add_payment(unique_id=unique_id,
                      user_id=user_id,
                      username=call.from_user.username,
                      amount=amount,
                      status=status,
                      bonus=bonus,
                      items_id=items_id)

    payment = await get_payment_unique(unique_id=unique_id)
    id_payment = payment.id

    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await bot.send_message(call.message.chat.id,
                           f'Счет:\n\n'
                           f'Сумма к оплате: {amount}\n'
                           f'После оплыты будет начилсенно {amount * 0.1} бонус(ов)\n\n'
                           f'Статус оплаты:  <b>Не оплачено!</b>',
                           reply_markup=await confirm_pay_kb(user_id=user_id,
                                                             id_payment=id_payment
                                                             ))


@dp.callback_query_handler(lambda call: "payConfirm_" in call.data)
async def pay_user_basket(call: types.CallbackQuery):
    await bot.answer_callback_query(callback_query_id=call.id, text=f'Товар оплачен.\n')
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = int(call.data.split('_')[1])
    id_payments = int(call.data.split('_')[2])
    new_status = 'paid'

    payment = await get_payment(id_payments=id_payments)
    user = await get_user(user_id)
    await change_user_balance(user_id, balance=user.balance + payment.bonus)
    await change_status_payment(id_payments, status=new_status)
    await delete_user_basket(user_id)

    await bot.send_message(call.message.chat.id,
                           f'Оплата прошла успешно!\n'
                           f'Спасибо за покупку!\n',
                           reply_markup=await main_menu())
    await bot.send_message(admins[0],
                           f'Пользователь совершил покупку:\n\n'
                           f'Пользователь:\n'
                           f'       ник: @{payment.username}\n'
                           f'       id: {user_id}\n\n'
                           f'Заказ:\n'
                           f'       id товара(через запятую): {payment.items_id}\n'
                           f'       На сумму: {payment.amount} руб.\n'
                           f'       Начисленно бонусов: {payment.bonus}\n\n'
                           f'Статус заказа:\n'
                           f'       {new_status}'
                           )
