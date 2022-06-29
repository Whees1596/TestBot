from aiogram import types
from loader import dp, bot
from keyboards.inline.support_inline_kb import support_kb


@dp.message_handler(text="Поддержка")
async def user_profile(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id,
                           f'Напиши нам, если у тебя проблема!\n\n'
                           f'Наши специалисты:',
                           reply_markup=await support_kb()
                           )