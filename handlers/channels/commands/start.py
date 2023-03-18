from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit


@rate_limit(2, '/start')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], text='/start')
async def command_start(message: types.Message):
    await message.answer('Всем привет')