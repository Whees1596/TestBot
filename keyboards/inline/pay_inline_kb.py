from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def confirm_pay_kb(user_id, id_payment) -> InlineKeyboardMarkup:
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Подтвердить оплату',
                                     callback_data=
                                     f'payConfirm_{user_id}_{id_payment}'),
            ]
        ]
    )
    return keyboard