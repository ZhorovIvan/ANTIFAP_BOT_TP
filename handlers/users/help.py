from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit


@rate_limit(5, '/help_user')
@dp.message_handler(chat_type=[ChatType.PRIVATE], commands=['help'])
async def help_user(message: types.Message):
    await message.answer('Бот напиши анекдот - Пишет блять анекдот \n'
                         'Бот напиши тост - Пишет блять тост \n'
                         'Бот извинись - Пишет блять прости')