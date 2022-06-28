from aiogram import types
from loader import dp, bot
from utils.db_api import quick_commands as commands

BOT_NICKNAME = 'ggtestgg_bot'


@dp.message_handler(text="Кабинет")
async def user_profile(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    user = await commands.get_user(message.from_user.id)
    count_refferals = await commands.count_refferals(message.from_user.id)
    await message.answer(f'Ваше имя: {user.name}\n\n'
                         f'Ваша реферальная ссылка: https://t.me/{BOT_NICKNAME}?start={message.from_user.id}\n\n'
                         f'Всего баллов: {user.balance}\n\n'
                         f'Всего приглашенных: {count_refferals}'
                         )
