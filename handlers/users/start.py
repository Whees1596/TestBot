import time

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from keyboards.default import main_menu
from keyboards.inline.registration_inline_kb import registration_kb, subscribe_kb
from utils.db_api import quick_commands as commands

CHANNEL_ID = '@ggtestggbotchannel'
REFFERER_ID = []


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    start_command = message.text
    if start_command == '/start':
        pass
    else:
        REFFERER_ID.append(int(start_command[7:]))
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        if await commands.get_user(message.from_user.id) is None:
            await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                                 f'Тебе нужно зарегистрироваться.',
                                 reply_markup=await registration_kb()
                                 )
        else:
            await message.answer(f'Привет, {message.from_user.full_name}!\n\n',
                                 reply_markup=await main_menu()
                                 )
    else:
        await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                             f'Для регистрации необходимо подписаться на канал!',
                             reply_markup=await subscribe_kb()
                             )


@dp.callback_query_handler(text='subDone')
async def sub_done(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)):
        if await commands.get_user(call.from_user.id) is None:
            await call.message.answer(f'{call.from_user.full_name}\n\n'
                                      f'Тебе нужно зарегистрироваться.',
                                      reply_markup=await registration_kb()
                                      )
        else:
            await call.message.answer(f'Привет, {call.from_user.full_name}!\n\n',
                                      reply_markup=await main_menu()
                                      )
    else:
        await call.message.answer(f'{call.from_user.full_name}\n\n'
                                  f'Для регистрации необходимо подписаться на канал!',
                                  reply_markup=await subscribe_kb()
                                  )


@dp.callback_query_handler(text='registrDone')
async def registr_done(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if len(REFFERER_ID) != 0:
        if REFFERER_ID[0] != call.from_user.id:
            await commands.add_user(user_id=call.from_user.id, name=call.from_user.full_name, referal_id=REFFERER_ID[0])
            await call.message.answer(f'{call.from_user.full_name}, регистрация прошла успешно!\n\n'
                                      f'Тебе доступен весь функционал!',
                                      reply_markup=await main_menu()
                                      )
            try:
                await bot.send_message(REFFERER_ID[0],
                                       f'По вашей ссылке зарегистрировался новый пользователь!\n\n'
                                       f'Вам начислено 100 баллов!')
                user = await commands.get_user(REFFERER_ID[0])
                await commands.change_user_balance(REFFERER_ID[0], balance=user.balance + 100)
            except:
                pass
        else:
            await bot.send_message(call.from_user.id,
                                   f'Регистрация по собственной ссылке запрещена!!\n\n'
                                   f'Вы будете зарегистрированы без реферала!'
                                   )
            time.sleep(3)
            await commands.add_user(user_id=call.from_user.id, name=call.from_user.full_name)
            await call.message.answer(f'{call.from_user.full_name}, регистрация прошла успешно!\n\n'
                                      f'Тебе доступен весь функционал!',
                                      reply_markup=await main_menu()
                                      )
    else:
        await commands.add_user(user_id=call.from_user.id, name=call.from_user.full_name)
        await call.message.answer(f'{call.from_user.full_name}, регистрация прошла успешно!\n\n'
                                  f'Тебе доступен весь функционал!',
                                  reply_markup=await main_menu()
                                  )
