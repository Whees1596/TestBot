from aiogram import types
from loader import dp, bot
from utils.db_api import quick_commands as commands


@dp.message_handler(text="Поддержка")
async def user_profile(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)