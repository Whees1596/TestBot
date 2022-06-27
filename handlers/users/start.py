from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from keyboards.default import main_menu
from keyboards.inline.registration_inline_kb import registration_kb

CHANNEL_ID = '@ggtestggbotchannel'


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                             f'Поздравляю с успешной регистрацией.',
                             reply_markup=await main_menu()
                             )
    else:
        await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                             f'Для регистрации необходимо подписаться на канал!',
                             reply_markup=await registration_kb()
                             )


@dp.callback_query_handler(text='subDone')
async def sub_done(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)):
        await call.message.answer(f'Привет, {call.from_user.full_name}!'
                                  f'Поздравляю с успешной регистрацией.',
                                  reply_markup=await main_menu()
                                  )
    else:
        await call.message.answer(f'Привет, {call.from_user.full_name}!\n\n'
                                  f'Для регистрации необходимо подписаться на канал!',
                                  reply_markup=await registration_kb()
                                  )
