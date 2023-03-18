from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit
import random

@rate_limit(5, 'apology_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='Бот извинись')
async def command_apology(message: types.Message):
    text_message = 'Прости ' if random.randint(0, 1) == 1 else 'Пошёл нахер ' + message.from_user.full_name
    await message.reply(text_message)