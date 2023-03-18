from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit


@rate_limit(5, '/start')
@dp.message_handler(chat_type=[ChatType.PRIVATE], text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}')